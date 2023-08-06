import pandas as pd

from typing import Optional
from entities.const import ConnectorType
from entities.sf_raw_data_models import Date
from storage.read import Reader


class DateStorage():
    """
    class to get the latest fk dim date based on passed value date
    """
    def __init__(
        self
    ) -> None:
        self.reader = Reader(
            connector=ConnectorType.SNOWFLAKE,
            user_id="ginevra.berti.mei@nbim.no"
        )

    def _set_query(self, date: Optional[str] = None):
        date_condition = """ SET DATE = CURRENT_TIMESTAMP::DATE """
        if date:
            date_condition = f""" SET DATE = TO_DATE('{date}') """
        return f""" {date_condition};
            SELECT
                VALUE_DATE::DATE AS VALUE_DATE,
                PREV_WORK_DAY::DATE AS FK_DIM_DATE,
                FIRST_WORK_DAY_MONTH::DATE AS FIRST_WORK_DAY_MONTH,
                LAST_WORK_DAY_MONTH::DATE AS LAST_WORK_DAY_MONTH,
                LAST_WORK_DAY_PREV_MONTH::DATE AS LAST_WORK_DAY_PREV_MONTH
            FROM
                PROD.BM.BM_DATE
            WHERE
                VALUE_DATE = $DATE
            """

    def _post_process(self, data: pd.DataFrame):
        # format cols
        data.columns = data.columns.str.lower()
        # reformat data for validation
        data = data.to_dict(orient="records")
        # validate data
        validated = []
        for cmp in data:
            validated.append(Date(**cmp))
        return validated

    def get(self, date: Optional[str] = None):
        q = self._set_query(date)
        data = self.reader.query_snowflake(query=q)
        return self._post_process(data)
