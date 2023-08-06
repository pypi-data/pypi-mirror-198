import os
from typing import List, Optional

import pandas as pd
from entities.const import ConnectorType, Const
from entities.sf_raw_data_models import ClassificationData
from storage.read import Reader

script_dir = os.path.dirname(__file__) + "\\queries\\"


class Classifications():
    """
    this class returns a list of ClassificationData objects
    """
    def __init__(
        self, db: Optional[str] = "PROD.NBIM_DM.INSTRUMENT"
    ) -> None:
        self.reader = Reader(
            connector=ConnectorType.SNOWFLAKE,
            user_id="ginevra.berti.mei@nbim.no"
        )
        self.db = db

    def _set_query(self, file_name, date):

        file_path = os.path.join(script_dir, file_name)
        fd = open(file_path, 'r')
        sql_q = fd.read()
        fd.close()

        if date:
            date_condition = f""" SET DATE = TO_DATE('{date}') """
        else:
            date_condition = """ SET DATE = CURRENT_TIMESTAMP::DATE """
        return f""" {date_condition}; {sql_q} """

    def _post_process(self, data: pd.DataFrame, as_df: bool = False):
        # format cols
        data.columns = data.columns.str.lower()
        # check if there are any duplicated values and only keep first
        # NOTE: this is not ideal as removal is arbitraty
        data = data.loc[~data[Const.ORG_CODE].duplicated(keep="first")]
        # make data a dictionary
        data = data.to_dict(orient="records")
        # validate data
        validated = [ClassificationData(**i) for i in data]
        if as_df:
            df = pd.DataFrame([i.dict() for i in validated]).set_index(Const.ORG_CODE, inplace=False)
            return df
        return validated

    def get(
        self, fields: List[str] = [], as_df: bool = False, date: Optional[str] = None
    ):
        # build query
        q = self._set_query("classifications.sql", date)
        # query
        data = self.reader.query_snowflake(query=q)
        # post process data
        data = self._post_process(data, as_df)
        # terminate connection
        self.reader.terminate()
        return data
