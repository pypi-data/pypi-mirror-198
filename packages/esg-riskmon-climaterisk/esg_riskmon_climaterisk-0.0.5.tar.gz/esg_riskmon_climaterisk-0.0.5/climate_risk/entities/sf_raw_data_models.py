from datetime import date, datetime
from typing import List, Optional

import numpy as np
from entities.cafeprod_fields import AttributionTypes
from entities.calculation_models import TrucostDataQuality
from entities.validators import (validate_float,
                                                  validate_make_millions,
                                                  validate_sectors,
                                                  validate_sign, validate_year)
from pydantic import BaseModel, root_validator, validator

"""
these models are used for data taken from the database in SNOWFLAKE.

their aim is to do basic checks and fill missing data as necessary.
some models need to be expanded based on the final state of the tables in snowflake
"""


class BaseIdentifiers(BaseModel):
    organisation_code: str
    organisation_name: Optional[str]
    fk_dim_date: Optional[date]

    sedol: Optional[str]
    isin: Optional[str]
    ticker: Optional[str]

    # _normalize = validator('isins', pre=True, allow_reuse=True)(normalise)


class FundamentalsSF(BaseIdentifiers):
    # mcap_usd: Optional[float] = np.nan
    proxy_revenue: Optional[float] = np.nan
    evic_nok: Optional[float] = np.nan

    _normalize = validator('evic_nok', pre=True, allow_reuse=True)(validate_make_millions)
    _normalize = validator('proxy_revenue', pre=True, allow_reuse=True)(validate_make_millions)


class EmissionsSF(BaseModel):
    emissions_tonnes_s1: Optional[float] = np.nan
    emissions_tonnes_s2: Optional[float] = np.nan
    emissions_tonnes_s12: Optional[float] = np.nan
    emissions_tonnes_s123: Optional[float] = np.nan

    report_date: Optional[float] = np.nan

    _valid = validator('report_date', pre=True, allow_reuse=True)(validate_year)
    # _valid = validator('emissions_tonnes_s1', pre=True, allow_reuse=True)(validate_sign)
    # _valid = validator('emissions_tonnes_s2', pre=True, allow_reuse=True)(validate_sign)

    @root_validator(pre=True)
    def validate_values(cls, values):
        # make scope 12 and 123
        try:
            values["emissions_tonnes_s12"] = float(
                values.get("emissions_tonnes_s1", np.nan)
                ) + float(values.get("emissions_tonnes_s2", np.nan))
        except Exception:
            values["emissions_tonnes_s12"] = np.nan

        try:
            values["emissions_tonnes_s123"] = float(
                values.get("emissions_tonnes_s12", np.nan)
            ) + float(values.get("emissions_tonnes_s3", np.nan))
        except Exception:
            values["emissions_tonnes_s123"] = np.nan

        return values


class ClassificationData(BaseIdentifiers):
    industry_level_1: Optional[str]
    industry_level_2: Optional[str]
    industry_level_3: Optional[str]
    industry_level_4: Optional[str]
    country_of_nbim: Optional[str]

    _normalize = validator(
        'industry_level_1', "industry_level_2", "industry_level_3", "country_of_nbim",
        pre=True, allow_reuse=True
    )(validate_sectors)


class ConstituentsEqBm(BaseIdentifiers):
    weight: float
    pf_weight: Optional[float]
    ownership: Optional[float]
    nav_nok: Optional[float]
    identifier: Optional[str]
    sedol: Optional[str]

    _normalize = validator(
        'weight',
        pre=True, allow_reuse=True
    )(validate_float)

    # _normalize = validator('nav_nok', pre=True, allow_reuse=True)(validate_make_millions)

    @root_validator(pre=True)
    def validate_ownership(cls, values):
        values["pf_weight"] = values["weight"]
        values["sedol"] = values["identifier"]
        return values


class ConstituentsEqPf(BaseIdentifiers):
    pf_weight: float
    nav_nok: float
    total_shares_outstanding: float
    cfd_pair_id: int
    conv_factor: float
    face_value_holding: float
    attribution: Optional[float]
    ownership: float
    portfolio_code: Optional[str]

    _normalize = validator(
        'pf_weight',  # 'pf_ownership',
        pre=True, allow_reuse=True
    )(validate_float)

    # _normalize = validator('nav_nok', pre=True, allow_reuse=True)(validate_make_millions)

    @root_validator(pre=True)
    def validate_ownership(cls, values):
        if values["total_shares_outstanding"] == 0:
            af = 0
        elif values["face_value_holding"] < 0 and values["cfd_pair_id"] != 0:
            af = 0
        else:
            af = values["face_value_holding"] * values["conv_factor"] / values["total_shares_outstanding"]
        values["ownership"] = af
        return values


class ConstituentsFiPf(BaseIdentifiers):
    pf_weight: float
    nav_nok: float
    attribution: Optional[float]
    ownership: float

    _normalize = validator(
        'pf_weight',
        pre=True, allow_reuse=True
    )(validate_float)

    # _normalize = validator('nav_nok', pre=True, allow_reuse=True)(validate_make_millions)

    @root_validator(pre=True)
    def validate_ownership(cls, values):
        values["ownership"] = values["pf_ownership"]
        values["attribution"] = values["attribution_factor"]
        return values


class CarbonDisclosure(BaseModel):
    carbon_disclosure: Optional[float] = np.nan
    nbim_category: Optional[str] = TrucostDataQuality.UNKNOWN.value
    nbim_numerical: Optional[float] = 5

    @root_validator(pre=True)
    def validate_values(cls, values):
        values["nbim_numerical"] = TrucostDataQuality.to_enum(values["nbim_category"]).to_int()
        return values


class TrucostData(
    ClassificationData, EmissionsSF, CarbonDisclosure
):
    turnover_usd_mln: Optional[float] = np.nan
    proxy_revenue: Optional[float] = np.nan
    evic_nok: Optional[float] = np.nan


class SectorMedians(BaseModel):
    industry_level_1: str
    industry_level_2: str
    industry_level_3: str
    industry_level_4: str

    industry_level_1_intensity_s1_median: Optional[float]
    industry_level_2_intensity_s1_median: Optional[float]
    industry_level_3_intensity_s1_median: Optional[float]
    industry_level_4_intensity_s1_median: Optional[float]
    universe_intensity_s1_median: Optional[float]

    industry_level_1_intensity_s2_median: Optional[float]
    industry_level_2_intensity_s2_median: Optional[float]
    industry_level_3_intensity_s2_median: Optional[float]
    industry_level_4_intensity_s2_median: Optional[float]
    universe_intensity_s2_median: Optional[float]

    industry_level_1_emissions_tonnes_s1_median: Optional[float]
    industry_level_2_emissions_tonnes_s1_median: Optional[float]
    industry_level_3_emissions_tonnes_s1_median: Optional[float]
    industry_level_4_emissions_tonnes_s1_median: Optional[float]
    universe_emissions_tonnes_s1_median: Optional[float]

    industry_level_1_emissions_tonnes_s2_median: Optional[float]
    industry_level_2_emissions_tonnes_s2_median: Optional[float]
    industry_level_3_emissions_tonnes_s2_median: Optional[float]
    industry_level_4_emissions_tonnes_s2_median: Optional[float]
    universe_emissions_tonnes_s2_median: Optional[float]

    n_records_industry_level_1: float
    n_records_industry_level_2: float
    n_records_industry_level_3: float
    n_records_industry_level_4: float

    @root_validator(pre=True)
    def validate_values(cls, values):
        # only keep medians when they are based on sample size >= 50
        for n in [1, 2, 3, 4]:
            if values[f"n_records_industry_level_{n}"] < 50:
                values[f"industry_level_{n}_intensity_s1_median"] = np.nan
                values[f"industry_level_{n}_intensity_s2_median"] = np.nan
                values[f"industry_level_{n}_emissions_tonnes_s1_median"] = np.nan
                values[f"industry_level_{n}_emissions_tonnes_s2_median"] = np.nan
        return values


class EmissionsDates(BaseIdentifiers):
    # used for outliers
    file_start_date: date
    file_end_date: date


class ClassifiedEmissions(
    TrucostData,
    ClassificationData,
    CarbonDisclosure
):
    proxy_median_intensity_s1: Optional[float] = np.nan
    proxy_median_intensity_s2: Optional[float] = np.nan
    proxy_median_intensity_s3: Optional[float] = np.nan
    data_quality: Optional[str] = None


class PortCompanyFootprintData(
    ClassifiedEmissions
):
    # NOTE: cannot inherit from FundamentalsSF because
    # of validator converting to millions
    ownership: Optional[float]
    attribution: Optional[float]
    pf_weight: Optional[float]
    nav_nok: Optional[float]
    mcap_usd: Optional[float] = np.nan
    turnover_usd_mln: Optional[float] = np.nan
    evic_nok: Optional[float] = np.nan
    portfolio_code: Optional[str]

    # _normalize = validator('nav_nok', pre=True, allow_reuse=True)(validate_make_millions)


class MsciLowCarbonTransitionScore(BaseModel):
    issuer_name: str
    issuer_sedol: Optional[str]
    issuer_isin: Optional[str]
    cbn_lct_category: Optional[str]


class Date(BaseModel):
    fk_dim_date: date
    value_date: date
    first_work_day_month: date
    last_work_day_month: date
    last_work_day_prev_month: date


class Outliers(BaseModel):
    organisation_code: str
    report_date: int
    description: str
    file_start_date: date
    file_end_date: date
    inserted: date
    inserted_by: str


class WaterfallWACI(BaseModel):
    type: str
    type_port: Optional[str]
    type_order: int
    waci_scope_1_2: float

    @root_validator(pre=True)
    def validate_values(cls, values):
        values["type_port"] = AttributionTypes.to_enum(values["type"])
        return values


class CompareMetrics(BaseModel):
    industry_level_1: str
    weight: float
    financed_12: float
    owned_12: float
    waci_12: float
    rank_waci: int
    rank_financed: int
    rank_owned: int


class MsciITR(BaseModel):
    issuer_id: Optional[str]
    issuer_name: Optional[str]
    issuer_sedol: Optional[str]
    issuer_isin: Optional[str]
    s1_itr: Optional[float]
    s2_itr: Optional[float]
    s3_itr: Optional[float]
    itr_start_date: date
    itr: float
