from enum import Enum

"""
all enumerators are fields in the db.
These constants are meant for snowflake data.
It's work in progress as we migrate and fields_cafeprod will then be deprecated
"""


class IdentifierRaw(Enum):
    ORG_CODE = "organisation_code"
    FK_DIM_DATE = "fk_dim_date"

    TICKER = "ticker"

    @classmethod
    def to_list(cls):
        return [i.value for i in cls]


class TrucostRaw(Enum):
    # ORG_CODE = "organisation_code"

    REPORT_YEAR = "report_date"
    DISCLOSURE = "carbon_disclosure"

    SCOPE_1 = "emissions_tonnes_s1"
    SCOPE_2 = "emissions_tonnes_s2"
    SCOPE_3 = "emissions_tonnes_s3"

    REVENUE = "turnover_usd_mln"

    @classmethod
    def to_list(cls):
        return [i.value for i in cls]


class CompositionEqBm(Enum):
    IDENTIFIER = "identifier"
    OWNERSHIP_MF = "ownership"
    NAV_NOK = "nav_nok"
    WEIGHT_MF = "weight"

    @classmethod
    def to_list(cls):
        return [i.value for i in cls]


class CompositionEqPf(Enum):
    ASSET_CLASS = "asset_class"
    SEDOL = "sedol"
    PORTFOLIO_CODE = "portfolio_code"
    CONVERSION_FACTOR = "conv_factor"
    FACE_VALUE_HOLDING = "face_value_holding"
    TOTAL_SHARES_OUTSTANDING = "total_shares_outstanding"
    NAV_NOK = "nav_nok"
    PF_WEIGHT = "pf_weight"
    CFD_PAIR_ID = "cfd_pair_id"

    @classmethod
    def to_list(cls):
        return [i.value for i in cls]


class CompositionFiPf(Enum):
    ASSET_CLASS = "asset_class"
    SEDOL = "sedol"
    NAV_NOK = "nav_nok"
    PF_WEIGHT = "pf_weight"
    ATTRIBUTION = "attribution_factor"
    OWNERSHIP = "pf_ownership"

    @classmethod
    def to_list(cls):
        return [i.value for i in cls]
