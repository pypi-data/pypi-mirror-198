import os
import numpy as np
import pandas as pd

from typing import List, Optional

from entities.const import ConnectorType, Const
from entities.sf_raw_data_models import (ClassifiedEmissions, TrucostData)
from entities.snowflake_fields import TrucostRaw
from storage.flexi import FlexiStorage
from storage.medians import MedianStorage
from storage.read import Reader


class Emissions():
    """
    this class returns a list of TrucostDataRaw objects
    """
    def __init__(
        self,
        db: Optional[str] = "PROD.INT_RISKMON.TRUCOST_CONSOLIDATED",
        year: Optional[int] = None
    ) -> None:
        self.reader = Reader(
            connector=ConnectorType.SNOWFLAKE,
            user_id="ginevra.berti.mei@nbim.no"
        )
        self.db = db
        self.year = year

    def _set_fields(self, fields: List[str] = []):
        fields.extend(TrucostRaw.to_list())
        fields.extend([Const.ORG_CODE])
        return fields

    def _build_query(self, fields, condition, date: Optional[str] = None):
        final_fields = ", ".join(fields)
        if date is None:
            date = 'CURRENT_TIMESTAMP'
        return f"""
                SELECT
                    {final_fields}
                FROM
                    {self.db}
                WHERE
                        {condition}
                        START_DATE  <=   CURRENT_TIMESTAMP
                    AND
                        END_DATE    >   CURRENT_TIMESTAMP
                    AND
                        ERROR_DUMMY_VARIABLE != 0
                """

    def _build_query_ri(self, date: Optional[str] = None):
        script_dir = os.path.dirname(__file__) + "\\queries\\"
        file_path = os.path.join(script_dir, "emissions_RI.sql")
        fd = open(file_path, 'r')
        sql_q = fd.read()
        fd.close()

        if date is None:
            date_condition = "set DATE = CURRENT_TIMESTAMP::DATE"
        else:
            date_condition = f"set DATE = TO_DATE('{date}')"

        set_date = f"""{date_condition}; set ALLOWED_YEARS = YEAR($DATE) - 2"""

        return f"""{set_date}; {sql_q}"""

    def _set_condition(self, id_field: Optional[str] = None, ids: Optional[List[str]] = []):
        year_condition = f"report_date = {str(self.year)}" if self.year else None
        ids_condition = f"{id_field} in {tuple(ids)}" if ids else None

        conds = [year_condition, ids_condition]
        if year_condition and ids_condition:
            return f"{year_condition} AND {ids_condition}"

        try:
            unique_cond = next(c for c in conds if c is not None)
        except StopIteration:
            return ""
        return f"{unique_cond} AND "

    def _post_process(
        self, data: pd.DataFrame, as_df: bool = False, cover: pd.DataFrame = None
    ):
        # format cols
        data.columns = data.columns.str.lower()
        # get a measure of missing emissions based on portfolio data
        if cover is not None:
            data = data.merge(
                cover,
                left_on=Const.ORG_CODE, right_index=True, how="right"
            )
            print("!!!! WARNING: REDUCING EMISSIONS BY PORTFOLIO COMPANIES !!!!")
        # reformat data for validation
        data = data.to_dict(orient="records")
        # validate data
        validated = [TrucostData(**i) for i in data]
        # reformat data
        if as_df:
            df = pd.DataFrame([i.dict() for i in validated])
            # if any column has all nans, drop
            df = df.dropna(axis=1, how='all')
            df.set_index(Const.ORG_CODE, inplace=True)
            return df
        return validated

    def _post_process_classified(self, data: pd.DataFrame, as_df: bool = False):
        data.reset_index(inplace=True)
        # reformat data for validation
        data = data.to_dict(orient="records")
        # validate data
        validated = [ClassifiedEmissions(**i) for i in data]
        # reformat data
        if as_df:
            df = pd.DataFrame([i.dict() for i in validated])
            df.set_index(Const.ORG_CODE, inplace=True)
            return df
        return validated

    def _fill_proxy_revenue(self, clf_med_emis_df):
        """
        makes sure if we have revenue data from any source, we use it
        """
        # get proxy revenue
        clf_med_emis_df["backfilled_revenue"] = np.where(
            clf_med_emis_df["turnover_usd_mln"].isna(),
            clf_med_emis_df["proxy_revenue"],
            clf_med_emis_df["turnover_usd_mln"]
        )
        return clf_med_emis_df

    def _backfill(self, clf_med_emis_df, scope):
        """
        makes sure every company has an emission value, or an intensity median value, or an emission median value
        also adds desription of data quality
        """
        # case 1: revenue and emissions both not available -> use intensity median
        # case 2: revenue is nan but emissions exist -> use intensity median
        # hence: whatever emissions, if revenue is nan we cannot compute intensity from emissions, so we need to use median
        clf_med_emis_df[f"proxy_median_intensity_{scope}"] = np.where(
            clf_med_emis_df["backfilled_revenue"].isna(),
            clf_med_emis_df[f"intensity_{scope}_use"],
            np.nan
        )
        # data quality adds
        clf_med_emis_df["data_quality"] = "Trucost Provided"
        clf_med_emis_df["data_quality"] = np.where(
            clf_med_emis_df["backfilled_revenue"].isna(),
            "Intensity Median",
            clf_med_emis_df["data_quality"]
        )

        # case 3: revenue exists but emissions is nan -> sector intensity median * company revenue
        # if emissions tonnes are not available, use intensity and revenue to reverse engineer emissions
        clf_med_emis_df[f"median_int_based_emis_{scope}"] = np.where(
            (clf_med_emis_df[f"emissions_tonnes_{scope}"].isna() & ~clf_med_emis_df["backfilled_revenue"].isna()),
            clf_med_emis_df[f"intensity_{scope}_use"] * clf_med_emis_df["backfilled_revenue"],
            clf_med_emis_df[f"emissions_tonnes_{scope}"]
        )
        # data quality adds
        clf_med_emis_df["data_quality"] = np.where(
            (clf_med_emis_df[f"emissions_tonnes_{scope}"].isna() & ~clf_med_emis_df["backfilled_revenue"].isna()),
            "Intensity median x company revenue",
            clf_med_emis_df["data_quality"]
        )
        # case 4: median based emissions (int*rev) could not be computed because of whatever reason
        # -> use emission medians
        clf_med_emis_df[f"median_int_based_emis_{scope}"] = np.where(
            clf_med_emis_df[f"median_int_based_emis_{scope}"].isna(),
            clf_med_emis_df[f"emissions_tonnes_{scope}_use"],
            clf_med_emis_df[f"median_int_based_emis_{scope}"]
        )
        # data quality adds
        clf_med_emis_df["data_quality"] = np.where(
            clf_med_emis_df[f"median_int_based_emis_{scope}"].isna(),
            "Emission Median",
            clf_med_emis_df["data_quality"]
        )
        return clf_med_emis_df

    def _calc_backfill_median(self, clf_med_emis_df):
        """
        general handling of missing data for revenue and emissions
        """
        # revenue
        clf_med_emis_df = self._fill_proxy_revenue(clf_med_emis_df)

        # emissions
        clf_med_emis_df = self._backfill(clf_med_emis_df, "s1")
        clf_med_emis_df = self._backfill(clf_med_emis_df, "s2")

        # drop original emissions and replace with newly backfilled
        clf_med_emis_df = clf_med_emis_df.drop(columns=["emissions_tonnes_s1", "emissions_tonnes_s2", "turnover_usd_mln"])
        clf_med_emis_df = clf_med_emis_df.rename(columns={
            "median_int_based_emis_s1": "emissions_tonnes_s1",
            "median_int_based_emis_s2": "emissions_tonnes_s2",
            "backfilled_revenue": "turnover_usd_mln"
        })
        return clf_med_emis_df

    def _add_sector_medians(
        self, classified_emissions, date
    ):
        classified_emissions.reset_index(inplace=True)
        # get medians
        medians_storage = MedianStorage(date=date)
        medians_df = medians_storage.get(as_df=True)

        # add universe to classified emissions:
        universe_cols = [col for col in medians_df.columns if 'universe' in col]
        universe_values = medians_df[universe_cols].drop_duplicates()
        universe_values = universe_values.to_dict(orient="records")
        for k, v in universe_values[0].items():
            classified_emissions[k] = v

        # merge by all icb levels
        clf_med_emis_df = medians_storage.smart_merge(
            icb_level=Const.ICB_1, data=classified_emissions, sector_medians=medians_df
        )
        clf_med_emis_df = medians_storage.smart_merge(
            icb_level="industry_level_2", data=clf_med_emis_df, sector_medians=medians_df
        )
        clf_med_emis_df = medians_storage.smart_merge(
            icb_level="industry_level_3", data=clf_med_emis_df, sector_medians=medians_df
        )
        clf_med_emis_df = medians_storage.smart_merge(
            icb_level="industry_level_4", data=clf_med_emis_df, sector_medians=medians_df
        )

        # create fields to use for each intensity, emissions median for each scope
        clf_med_emis_df = medians_storage._to_use(clf_med_emis_df, var="intensity", scope="s1")
        clf_med_emis_df = medians_storage._to_use(clf_med_emis_df, var="intensity", scope="s2")
        clf_med_emis_df = medians_storage._to_use(clf_med_emis_df, var="emissions_tonnes", scope="s1")
        clf_med_emis_df = medians_storage._to_use(clf_med_emis_df, var="emissions_tonnes", scope="s2")

        # reverse calculate emissions from sector median intensity and company specific turnover
        # replace emissions with calculated median based turnover
        clf_med_emis_df = self._calc_backfill_median(clf_med_emis_df)
        return clf_med_emis_df

    def _add_disclosure(self, emission_data):
        # add disclosure data to emissions
        disclosure_storage = FlexiStorage(
            vendor="carbon_disclosure",
            sql_file="trucost_carbon_disc.sql"
        )
        c_disclosure = disclosure_storage.get(as_df=True)
        constituents_df = emission_data.merge(
            c_disclosure, how="left", right_on="carbon_disclosure", left_on="CARBON_DISCLOSURE"
        )
        return constituents_df

    def _query_emissions(
        self, fields: List[str] = [], ri_report: Optional[bool] = True,
        fk_dim_date: Optional[str] = None
    ):
        # build query
        q = self._build_query(
            fields=self._set_fields(fields),
            condition=self._set_condition(),
            date=fk_dim_date
        )
        if ri_report:
            q = self._build_query_ri(fk_dim_date)
        # query
        data = self.reader.query_snowflake(query=q)
        return data

    def get(
        self,
        fields: List[str] = [],
        cover: Optional[pd.DataFrame] = None,
        as_df: bool = True,
        ri_report: Optional[bool] = True,
        with_medians: bool = False,
        date: Optional[str] = None
    ) -> list[TrucostData]:
        # get emissions data
        data = self._query_emissions(fields, ri_report, fk_dim_date=date)
        # add disclosure data
        data = self._add_disclosure(data)
        # post process data
        data = self._post_process(
            data=data, as_df=as_df,
            cover=cover
        )
        # add medians if requested
        if with_medians:
            # add classification data (sectors)
            data = self._add_sector_medians(data, date)
            data = self._post_process_classified(data, as_df)
        # terminate connection
        self.reader.terminate()
        return data
