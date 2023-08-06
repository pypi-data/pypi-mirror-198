from enum import Enum

"""
all enumerators are fields in the db
this will be deprecated in facour of snowflake_fields.py
Some of these Enumerators will be migrated but could be changed
"""


class TrucostDataQuality(Enum):
    REPORTED = 'Emission reported by company'
    ESTIMATED_REPORT = 'Estimate of emission based on company report'
    MODELLED = 'Model estimate of emissions'
    UNDISCLOSED = 'Undisclosed Source'
    UNKNOWN = 'Unknown'

    @classmethod
    def to_list(cls):
        return [i.value for i in cls]

    def to_int(v):
        mapp = {
            v.REPORTED: 1,
            v.ESTIMATED_REPORT: 2,
            v.MODELLED: 3,
            v.UNDISCLOSED: 4,
            v.UNKNOWN: 5
        }
        return mapp[v]

    def to_enum(v):
        mapp = {
            k.value: k for k in TrucostDataQuality
        }
        if v in TrucostDataQuality.to_list():
            return mapp[v]
        return TrucostDataQuality.UNKNOWN


class AllowedSectors(Enum):
    INDUSTRIALS = 'Industrials'
    UTILITIES = 'Utilities'
    CONSUMER_DISCRETIONARY = 'Consumer Discretionary'
    FINANCIALS = 'Financials'
    TECHNOLOGY = 'Technology'
    ENERGY = 'Energy'
    BASIC_MATERIALS = 'Basic Materials'
    CONSUMER_STAPLES = 'Consumer Staples'
    HEALTH_CARE = 'Health Care'
    REAL_ESTATE = 'Real Estate'
    TELECOMMUNCATION = 'Telecommunications'
    # TODO: CHECK THIS, WHY DO WE HAVE IT?
    UNKNOWN = 'Unknown'
    UNDEFINED = "Undefined"

    @classmethod
    def to_list(cls):
        return [i.value for i in cls]


class AllowedTargets(Enum):
    """
    This Enumerator serves as allowed values for target data.
    There is a hirarchy and these values are not mutually exclusive:
    The hirarchy for this field is the following:
    sbti set, -> sbti committed -> msci set
    """
    MSCI_SET = "MSCI Target"
    SBTI_SET = "SBTi - Targets Set"
    SBTI_COMMITTED = "SBTi - Committed"

    @classmethod
    def to_list(cls):
        return [i.value for i in cls]


class TargetFlag(Enum):
    HAS_TARGET = "has_target"
    NO_TARGET = "no_target"


class PCAFSectors(Enum):
    INDUSTRIALS = 'Industrials'
    UTILITIES = 'Utilities'
    ENERGY = 'Energy'

    @classmethod
    def to_list(cls):
        return [i.value for i in cls]


class TrucostParams(Enum):
    REPORT_YEAR = "report_year"
    EMISSION_DATA = "emission_data_source"
    SCOPE_1 = "emission_scope_1"
    SCOPE_2 = "emission_scope_2"

    @classmethod
    def to_list(cls):
        return [cls.to_field(i) for i in cls]

    @classmethod
    def to_field(cls, v):
        if v not in [cls.SCOPE_1, cls.SCOPE_2]:
            return f"trucost_{v.value}"
        return v.value


class ClassificationParams(Enum):
    SECTOR = "industry_level_1"
    COUNTRY = "country_of_risk"
    ORG_CODE = "organisation_code"
    ORG_NAME = "organisation_name"
    WEIGHT = "pf_weight"
    ISINS = "isins"
    SEDOLS = "sedols"
    NAV_NOK = "nav_nok"
    NAV_USD = "nav_usd"
    OWNERSHIP = "ownership"
    MCAP_USD = "mcap_usd"
    EQ_VAL_NOK = "eq_nav_nok"
    PORT_VAL_NOK = "tot_nav_nok"
    TURNOVER_USD = "turnover_usd_mln"

    @classmethod
    def to_list(cls):
        return [i.value for i in cls]


class CountrySectorParams(Enum):
    INTENSITY = "carbon_intensity"
    WATER = "water"
    WASTE = "waste"
    BIODIVERSITY = "biodiversity"
    CLIMATE_CHANGE = "climate_change"
    HEALTH_SAFETY = "health_and_safety"
    HUMAN_CAPITAL = "human_capital"
    CHILD_LABOUR = "child_labour"
    CORRUPTION = "corruption"
    GOVERNANCE = "corporate_governance"
    E_SCORE = "e_score"
    S_SCORE = "s_score"
    G_SCORE = "g_score"
    ESG_SCORE = "esg_score"

    @classmethod
    def to_list(cls):
        return [cls.to_field(i) for i in cls]

    @classmethod
    def to_field(cls, v):
        return f"country_sector_{v.value}"


class MsciParams(Enum):
    IVA = "IVA_COMPANY_RATING"
    GOVERNANCE = "GOVERNANCE_PILLAR_SCORE"
    ENVIRONMENT = "ENVIRONMENTAL_PILLAR_SCORE"
    SOCIAL = "SOCIAL_PILLAR_SCORE"

    @classmethod
    def to_field(cls, v):
        return f"msci_{v.value}"

    @classmethod
    def to_list(cls):
        return [cls.to_field(i) for i in cls]


class RepRiskParams(Enum):
    PEAK_RRI = "peak_rri"
    RRI = "current_rri"

    @classmethod
    def to_field(cls, v):
        return f"reprisk_{v.value}"

    @classmethod
    def to_list(cls):
        return [cls.to_field(i) for i in cls]


class RRR(Enum):
    A = "A"
    AA = "AA"
    AAA = "AAA"
    B = "B"
    BB = "BB"
    BBB = "BBB"
    C = "C"
    CC = "CC"
    CCC = "CCC"
    D = "D"

    @classmethod
    def to_list(cls):
        return [i.value for i in cls]

    def to_int(v):
        maps = {
            RRR.A: 1,
            RRR.AA: 2,
            RRR.AAA: 3,
            RRR.BBB: 4,
            RRR.BB: 5,
            RRR.B: 6,
            RRR.CCC: 7,
            RRR.CC: 8,
            RRR.C: 9,
            RRR.D: 10
        }
        return maps[v]


class AttributionTypes(Enum):
    FREEFLOAT = 'FTSE All Cap'
    CTY = 'Country Factors'
    OFFSHORE = 'Removal of Offshore'
    MF = 'Ethical Exclusions'
    RBD_POST = 'Risk Based Divestments'
    OMVUSD = 'Full Universe'
    UNKNOWN = "Unknown"

    @classmethod
    def to_list(cls):
        return [i.name for i in cls]

    def to_enum(v):
        mapp = {
            k.name: k.value for k in AttributionTypes
        }
        if v in AttributionTypes.to_list():
            return mapp[v]
        return AttributionTypes.UNKNOWN.value
