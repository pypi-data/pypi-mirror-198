from enum import Enum

from storage.connect import SnowflakeConnector, SQLConnector

"""
constants that are used internally, and are not dependent necessarily on variable names from databases
"""


class ConnectorType:
    SQL = SQLConnector
    SNOWFLAKE = SnowflakeConnector


class Scopes(Enum):
    SCOPE_1 = "scope_1"
    SCOPE_2 = "scope_2"
    SCOPE_3 = "scope_3"
    SCOPE_12 = "scope_1_2"
    # TODO: consider uncommenting or making this field at later stages
    # SCOPE_123 = "scope_123"

    @classmethod
    def to_list(cls):
        return [i.value for i in cls]


class Const:
    WACI = "waci"
    TCE = "tce"
    OE = "oe"

    REV = "turnover_usd_mln"
    MCAP = "mcap_usd"
    EVIC = "evic_nok"

    ISIN = "isin"
    ORG_CODE = "organisation_code"

    ICB_1 = "industry_level_1"
    ICB_2 = "industry_level_2"


class AllowedTypes(Enum):
    EQ_PORTFOLIO = "equity"
    BENCHMARK = "benchmark"
    FI_PORTFOLIO = "fixed_income"
    FI_BENCHMARK = 'fixed_income_benchmark'
    FTSE = "ftse_all_cap"
