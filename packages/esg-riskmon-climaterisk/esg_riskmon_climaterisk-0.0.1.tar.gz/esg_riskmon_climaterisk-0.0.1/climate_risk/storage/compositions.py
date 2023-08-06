from typing import List, Optional

import pandas as pd
from entities.const import AllowedTypes, ConnectorType, Const
from entities.sf_raw_data_models import (ConstituentsEqBm,
                                                          ConstituentsEqPf,
                                                          ConstituentsFiPf)
from entities.snowflake_fields import (CompositionEqBm,
                                                        CompositionEqPf,
                                                        CompositionFiPf,
                                                        IdentifierRaw)
from storage.read import Reader


class Compositions():
    """
    this class retrieves portfolio compositions (pf/bm for eq)
    """
    def __init__(
        self, type: AllowedTypes = AllowedTypes.EQ_PORTFOLIO
    ) -> None:
        self.reader = Reader(
            connector=ConnectorType.SNOWFLAKE,
            user_id="ginevra.berti.mei@nbim.no"
        )
        self.type = type
        self.model_map = {
            AllowedTypes.BENCHMARK: ConstituentsEqBm,
            AllowedTypes.FI_PORTFOLIO: ConstituentsFiPf,
            AllowedTypes.EQ_PORTFOLIO: ConstituentsEqPf,
            AllowedTypes.FTSE: ConstituentsEqBm
        }
        mapp = {
            AllowedTypes.BENCHMARK: "GET_CLIM_MFEQ",
            AllowedTypes.FI_PORTFOLIO: "GET_CLIM_PFFI_WACI",
            AllowedTypes.EQ_PORTFOLIO: "GET_CLIM_PFEQ",
            AllowedTypes.FTSE: "GET_CLIM_MFEQ"
        }
        self.db = f"PROD.INT_RISKMON.{mapp[self.type]}"

    def _set_fields(self, fields: List[str]):
        field_map = {
            AllowedTypes.BENCHMARK: CompositionEqBm.to_list(),
            AllowedTypes.FI_PORTFOLIO: CompositionFiPf.to_list(),
            AllowedTypes.EQ_PORTFOLIO: CompositionEqPf.to_list(),
            AllowedTypes.FTSE: CompositionEqBm.to_list()
        }
        add_fields = field_map[self.type]
        fields.extend(add_fields)
        fields.extend(IdentifierRaw.to_list())
        return fields

    def _build_query(
        self,
        fields: List[str],
        fund: Optional[str] = "ROIL",
        date: Optional[str] = None
    ):
        final_fields = ", ".join(fields)
        fund_condition = f""" set FUND = '{fund}' """
        date_condition = f"""set DATE = TO_DATE('{date}')"""

        if date is None:
            date_condition = f"""
                            set DATE = (
                                SELECT
                                        MAX(FK_DIM_DATE)
                                FROM
                                        {self.db}
                            )
                            """

        query_map = {
            AllowedTypes.BENCHMARK:  self._benchmark_query(final_fields, 'MF'),
            AllowedTypes.FTSE:  self._benchmark_query(final_fields, 'CTY'),
            AllowedTypes.FI_PORTFOLIO: self._eq_portfolio_query(final_fields),
            AllowedTypes.EQ_PORTFOLIO: self._eq_portfolio_query(final_fields)
        }
        q = query_map[self.type]

        return f"""
                {date_condition};
                {fund_condition};
                {q}
        """

    def _eq_portfolio_query(self, final_fields):
        return f"""
                SELECT
                    {final_fields}
                FROM
                    {self.db}
                WHERE
                        FK_DIM_DATE = $DATE
                    AND
                        FUND = $FUND
                """

    def _benchmark_query(self, final_fields, type_benchmark):
        return f"""
            SELECT
                {final_fields}
            FROM
                {self.db}
            WHERE
                    TYPE = '{type_benchmark}'
                AND
                    FK_DIM_DATE = $DATE
            ORDER BY
                ORGANISATION_CODE DESC
        """

    def _post_process(self, data: pd.DataFrame, as_df: bool = False):
        # format cols
        data.columns = data.columns.str.lower()
        # reformat data for validation
        data = data.to_dict(orient="records")
        # validate data
        valid_model = self.model_map[self.type]
        validated = [valid_model(**i) for i in data]
        # reformat data
        if as_df:
            df = pd.DataFrame([i.dict() for i in validated]).set_index(Const.ORG_CODE, inplace=False)
            return df
        return validated

    def get(
        self,
        fields: List[str] = [],
        as_df: bool = False,
        date: Optional[str] = None
    ):
        # set fields
        req_fields = self._set_fields(fields)
        # build query
        q = self._build_query(
            fields=req_fields,
            date=date
        )
        # query
        data = self.reader.query_snowflake(query=q)
        # post process data
        data = self._post_process(data, as_df)
        return data
