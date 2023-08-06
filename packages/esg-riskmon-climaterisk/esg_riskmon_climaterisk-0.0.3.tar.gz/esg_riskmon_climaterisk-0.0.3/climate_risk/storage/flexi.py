import os
import pandas as pd

from typing import Optional
from entities.const import ConnectorType, Const
from entities.raw_data_models import (MSCIEmissions, TrucostEmissions)
from entities.sf_raw_data_models import (
    BaseIdentifiers, CarbonDisclosure, CompareMetrics, EmissionsDates,
    MsciITR, MsciLowCarbonTransitionScore, FundamentalsSF, Outliers,
    PortCompanyFootprintData, WaterfallWACI
)
from storage.read import Reader

script_dir = os.path.dirname(__file__) + "\\queries\\"


class FlexiStorage():
    """
    class to get any data based on a *required* sql file that sits in storage.queries
    data models for validations of some vendors' data are already provided - check MSCI
    perhaps Trucost needs update to relfect newest fields
    """
    def __init__(
        self,
        vendor: Optional[str] = "2021_RI",
        sql_file: Optional[str] = None
    ) -> None:
        self.reader = Reader(
            connector=ConnectorType.SNOWFLAKE,
            user_id="ginevra.berti.mei@nbim.no"
        )
        self.vendor = vendor
        self.sql_q = sql_file
        self.vendor_mod_map = {
            "msci": MSCIEmissions,
            "trucost": TrucostEmissions,
            "2021_RI": PortCompanyFootprintData,
            "carbon_disclosure": CarbonDisclosure,
            "fundamentals": FundamentalsSF,
            "get_latest_timestamp": EmissionsDates,
            "outliers": BaseIdentifiers,
            "get_all_outliers": Outliers,
            "waterfall_waci": WaterfallWACI,
            "compare_metrics": CompareMetrics,
            "msci_itr": MsciITR,
            "v_instrument": BaseIdentifiers,
            "msci_lcts": MsciLowCarbonTransitionScore
        }

    def _set_query(
        self, file_name: str,
        date: Optional[str] = None,
        report_year: Optional[int] = None
    ):
        # read query file
        file_path = os.path.join(script_dir, file_name)
        fd = open(file_path, 'r', encoding="UTF-8")
        sql_q = fd.read()
        fd.close()
        """
        NOTE: add date. if none; use current time stamp
        if not none, add used passed date
        if the query doesn't have a date variable, it won't be used
        """
        if date:
            date_condition = f""" SET DATE = TO_DATE('{date}') """
        else:
            date_condition = """ SET DATE = CURRENT_TIMESTAMP::DATE """
        return f""" {date_condition}; SET REPORT_YEAR = '{report_year}';
                {sql_q} """

    def _post_process(self, data: pd.DataFrame, as_df: bool):
        # format cols
        data.columns = data.columns.str.lower()
        # reformat data for validation
        data = data.to_dict(orient="records")
        validated = []
        for cmp in data:
            validated.append(self.vendor_mod_map[self.vendor](**cmp))

        if as_df:
            # create a dataframe of validated data and set organisation code as index
            df = pd.DataFrame([i.dict() for i in validated])
            df.set_index(Const.ORG_CODE, inplace=True) if Const.ORG_CODE in df.columns else df
            return df
        # return a validated dict
        return validated

    def get(self, as_df: Optional[bool] = True, date: Optional[str] = None, report_year: Optional[int] = None):
        q = self._set_query(self.sql_q, date, report_year)
        data = self.reader.query_snowflake(query=q)
        return self._post_process(data, as_df)
