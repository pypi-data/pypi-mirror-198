import os
import numpy as np
import pandas as pd

from typing import Optional
from entities.const import ConnectorType
from entities.sf_raw_data_models import SectorMedians
from storage.read import Reader

script_dir = os.path.dirname(__file__) + "\\queries\\"


class MedianStorage():
    """
    class to get any data based on a *required* sql file that sits in storage.queries
    only applies to SNOWFLAKE
    data models for validations of some vendors' data are already provided - check MSCI
    perhaps Trucost needs update to relfect newest fields
    """
    def __init__(
        self, date: Optional[str] = None
    ) -> None:
        self.reader = Reader(
            connector=ConnectorType.SNOWFLAKE,
            user_id="ginevra.berti.mei@nbim.no"
        )
        self.date = date

    def _set_query(self):
        file_path = os.path.join(script_dir, "sector_medians.sql")
        fd = open(file_path, 'r')
        sql_q = fd.read()
        fd.close()
        if self.date:
            date_condition = f""" SET DATE = TO_DATE('{self.date}') """
        else:
            date_condition = """ SET DATE = CURRENT_TIMESTAMP::DATE """
        return f""" {date_condition}; {sql_q}"""

    def _to_use(self, clf_med_emis_df: pd.DataFrame, var: str, scope: str):
        # identify most granular level of median to use for either intensity or emissions
        clf_med_emis_df[f"{var}_{scope}_use"] = np.where(
            clf_med_emis_df[f"industry_level_4_{var}_{scope}_median"].isna(),
            np.where(
                clf_med_emis_df[f"industry_level_3_{var}_{scope}_median"].isna(),
                np.where(
                    clf_med_emis_df[f"industry_level_2_{var}_{scope}_median"].isna(),
                    np.where(
                        clf_med_emis_df[f"industry_level_1_{var}_{scope}_median"].isna(),
                        clf_med_emis_df[f"universe_{var}_{scope}_median"],
                        clf_med_emis_df[f"industry_level_1_{var}_{scope}_median"]
                    ),
                    clf_med_emis_df[f"industry_level_2_{var}_{scope}_median"]
                ),
                clf_med_emis_df[f"industry_level_3_{var}_{scope}_median"]
            ),
            clf_med_emis_df[f"industry_level_4_{var}_{scope}_median"]
        )
        return clf_med_emis_df

    def _post_process(self, data: pd.DataFrame, as_df: bool):
        # format cols
        data.columns = data.columns.str.lower()
        # reformat data for validation
        data = data.to_dict(orient="records")
        # validate data
        validated = []
        for cmp in data:
            validated.append(SectorMedians(**cmp))
        if as_df:
            # create a dataframe of validated data and set organisation code as index
            df = pd.DataFrame([i.dict() for i in validated])
            return df
        # return a validated dict
        return validated

    def get(
        self, as_df: Optional[bool] = True,
        date: Optional[str] = None
    ):
        q = self._set_query()
        data = self.reader.query_snowflake(query=q)
        return self._post_process(data, as_df)

    def slice(
        self, icb_level: str, data: pd.DataFrame
    ):
        # split the dataframe into icb1, emissions_icb1, intensity_icb1; icb2, emissions_icb2, intensity_icb2
        match = [
            icb_level,
            f"{icb_level}_intensity_s1_median", f"{icb_level}_intensity_s2_median",
            f"{icb_level}_emissions_tonnes_s1_median", f"{icb_level}_emissions_tonnes_s2_median"
        ]
        icb_data = data[match].drop_duplicates()
        return icb_data

    def smart_merge(self, icb_level: str, data: pd.DataFrame, sector_medians: pd.DataFrame):
        # keep only icb level related info
        icb_data = self.slice(icb_level, sector_medians)
        # merge by icb level
        medians_data = icb_data.merge(data, how="right", right_on=icb_level, left_on=icb_level)
        return medians_data
