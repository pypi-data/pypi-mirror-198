from typing import List, Optional

import numpy as np
from entities.cafeprod_fields import (RRR, AllowedTargets,
                                                       TrucostDataQuality)
from entities.validators import (clean_msci, clean_RRR,
                                                  normalise,
                                                  validate_make_millions,
                                                  validate_tds, validate_year)
from pydantic import BaseModel, root_validator, validator

incomparables = ["nan", "None", None, np.nan]

"""
NOTE: these data models were made for cafeprod data. they will be replaced in the file sf_raw_data_models.py and this file will be deprecated

THESE ARE ONLY MODELS FOR DATA COMING FROM DB, WITH BASIC VALIDATIONS USED FOR MANIPULATIONS

CONTSTRUCTED MODELS ARE IN PROC_MODELS.PY AND USED FOR CALCULATIONS
"""


class BaseIdentifiers(BaseModel):
    organisation_code: Optional[str]
    organisation_name: Optional[str]
    sedols: Optional[str]
    isins: Optional[List[str]]

    # _normalize = validator('sedols', pre=True, allow_reuse=True)(normalise)
    _normalize = validator('isins', pre=True, allow_reuse=True)(normalise)


class Positioning(BaseModel):
    nav_nok: Optional[float] = None
    nav_usd: Optional[float] = None
    eq_nav_nok: Optional[float] = None
    tot_nav_nok: Optional[float] = None

    pf_weight: Optional[float] = None
    ownership: Optional[float] = None


class Classifications(BaseIdentifiers):
    industry_level_1: Optional[str] = None
    country_of_nbim: Optional[str] = None


class Fundamentals(BaseModel):
    mcap_usd: Optional[float] = None
    turnover_usd_mln: Optional[float] = None

    _normalize = validator('mcap_usd', pre=True, allow_reuse=True)(validate_make_millions)
    # TODO: decide here what validation for revenue


class CompanyEmissions(Classifications, Positioning, Fundamentals):
    emission_scope_1: Optional[float] = None
    emission_scope_2: Optional[float] = None
    emission_scope_1_2: Optional[float] = None

    trucost_emission_data_source: Optional[TrucostDataQuality] = None
    trucost_report_year: Optional[int] = None
    quality_score: Optional[int] = None

    _valid = validator('trucost_emission_data_source', pre=True, allow_reuse=True)(validate_tds)

    @root_validator(pre=True)
    def validate_values(cls, values):
        # make scope 12
        try:
            values["emission_scope_1_2"] = values.get("emission_scope_1", None) + values.get("emission_scope_2", None)
        except Exception:
            values["emission_scope_1_2"] = None
        return values


class Target(BaseModel):
    # sector: Optional[AllowedSectors] = None  # remove this and use it from emissions instead
    climate_target: Optional[AllowedTargets]
    nz_target: Optional[AllowedTargets]
    has_target: Optional[bool] = True

    @root_validator(pre=True)
    def validate_values(cls, values):
        # if a company has no target at all, it will be flagged as no target
        # if a company has both committed targets, it will be flagged as no target
        if not values.get("nz_target", None) and not values.get("climate_target", None):
            values["has_target"] = False
        elif values.get("nz_target") == AllowedTargets.SBTI_COMMITTED.value and values.get("climate_target") == AllowedTargets.SBTI_COMMITTED.value:
            values["has_target"] = False
        return values


class MSCIEmissions(BaseIdentifiers):
    msci_id: str
    msci_scope_1: Optional[float] = np.nan
    msci_scope_2: Optional[float] = np.nan
    msci_scope_3: Optional[float] = np.nan
    msci_reporting_year: Optional[int] = np.nan

    @validator('msci_scope_1', 'msci_scope_2', 'msci_scope_3', pre=True)
    def validate_scopes(cls, v):
        if isinstance(v, str):
            return float(v.replace(",", ""))
        return np.nan

    _valid = validator('msci_reporting_year', pre=True, allow_reuse=True)(validate_year)


class TrucostEmissions(BaseIdentifiers):
    emission_scope_1: Optional[float] = np.nan
    emission_scope_2: Optional[float] = np.nan
    emission_scope_1_2: Optional[float] = np.nan

    carbon_disclosure: Optional[float] = np.nan
    trucost_report_year: Optional[int] = np.nan
    trucost_emission_data_source: Optional[TrucostDataQuality] = None
    quality_score: Optional[int] = None

    @validator('emission_scope_1', 'emission_scope_2', 'carbon_disclosure', pre=True)
    def validate_scopes(cls, v):
        if isinstance(v, str):
            return float(v.replace(",", ""))
        elif isinstance(v, (int, float)):
            return v
        return np.nan

    _valid = validator('trucost_report_year', pre=True, allow_reuse=True)(validate_year)
    _valid = validator('trucost_emission_data_source', pre=True, allow_reuse=True)(validate_tds)

    @root_validator(pre=True)
    def validate_values(cls, values):
        # make scope 12
        try:
            values["emission_scope_1_2"] = values.get("emission_scope_1", None) + values.get("emission_scope_2", None)
        except Exception:
            values["emission_scope_1_2"] = None
        return values


class CompanyTargets(BaseIdentifiers, Target):
    pass


class Company(CompanyEmissions, CompanyTargets):
    # TODO: include CompanyFundamentals once we use new fundamentals table
    pass

    @root_validator(pre=True)
    def validate_vals(cls, values):
        # make a new data disc category as integer
        if not isinstance(values["trucost_emission_data_source"], TrucostDataQuality):
            values["trucost_emission_data_source"] = TrucostDataQuality.to_enum(values["trucost_emission_data_source"])
        values["quality_score"] = values["trucost_emission_data_source"].to_int()
        return values


class ESG(BaseIdentifiers):
    msci_IVA_COMPANY_RATING: Optional[RRR]
    msci_SOCIAL_PILLAR_SCORE: Optional[float]
    msci_GOVERNANCE_PILLAR_SCORE: Optional[float]
    msci_ENVIRONMENTAL_PILLAR_SCORE: Optional[float]

    reprisk_peak_rri: Optional[float]
    reprisk_rating: Optional[RRR]

    rri: Optional[float]
    rrr: Optional[float]
    iva: Optional[float]

    _clean_msci = validator('msci_SOCIAL_PILLAR_SCORE', pre=True, allow_reuse=True)(clean_msci)
    _clean_msci = validator('msci_GOVERNANCE_PILLAR_SCORE', pre=True, allow_reuse=True)(clean_msci)
    _clean_msci = validator('msci_ENVIRONMENTAL_PILLAR_SCORE', pre=True, allow_reuse=True)(clean_msci)
    _clean_msci = validator('reprisk_peak_rri', pre=True, allow_reuse=True)(clean_msci)

    _clean_msci = validator('msci_IVA_COMPANY_RATING', pre=True, allow_reuse=True)(clean_RRR)
    _clean_msci = validator('reprisk_rating', pre=True, allow_reuse=True)(clean_RRR)
