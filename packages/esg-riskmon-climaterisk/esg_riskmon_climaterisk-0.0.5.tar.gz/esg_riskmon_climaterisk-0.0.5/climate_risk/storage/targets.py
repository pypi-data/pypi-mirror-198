import pandas as pd

from typing import Optional
from entities.const import ConnectorType, Const
from entities.raw_data_models import CompanyTargets
from storage.read import Reader


class Targets():
    """
    retrieves targets data, returns CompanyTargets objects
    TODO: query should be dynamic, use set_fields()
    TODO: post processing clean up think what you want to do here
    """
    def __init__(self) -> None:
        self.reader = Reader(
            connector=ConnectorType.SNOWFLAKE,
            user_id="ginevra.berti.mei@nbim.no"
        )

    def _default_query(self):
        return """
        SELECT
            organisation_code,
            nz_target,
            climate_target
        FROM
            PROD.MRT_CORP_GOV.NZ_TRACKER
        """

    def _set_fields(self):
        pass

    def _post_process(self, data: pd.DataFrame, as_df: bool):
        data.columns = data.columns.str.lower()
        # reformat data for validation
        data = data.to_dict(orient="records")
        # validate data
        validated = [CompanyTargets(**i) for i in data]
        # reformat data
        if as_df:
            df = pd.DataFrame([i.dict() for i in validated])
            df = df.drop_duplicates(subset="organisation_code", keep="first")
            df.set_index(Const.ORG_CODE, inplace=True)
            return df
        return validated

    def get(self, as_df: bool, query: Optional[str] = None):
        if not query:
            query = self._default_query()

        data = self.reader.query_snowflake(query=query)
        data = self._post_process(data, as_df)
        return data
