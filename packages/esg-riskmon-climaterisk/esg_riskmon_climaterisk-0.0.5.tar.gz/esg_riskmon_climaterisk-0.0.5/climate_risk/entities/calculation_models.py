from typing import Optional

import numpy as np
from entities.cafeprod_fields import TrucostDataQuality
from entities.raw_data_models import Classifications
from pydantic import BaseModel

"""
THESE ARE ONLY CONTSTRUCTED MODELS USED FOR CALCULATIONS

UNPROC_MODELS.PY IS FOR DATA MODELS FOR DATA COMING FROM DB, WITH BASIC VALIDATIONS USED FOR MANIPULATIONS
"""


class EmissionsScopes(BaseModel):
    scope_1: Optional[float]
    scope_2: Optional[float]
    scope_3: Optional[float]
    scope_1_2: Optional[float]

    @classmethod
    def _create_empty(cls):
        return cls(scope_1=np.nan, scope_2=np.nan, scope_3=np.nan, scope_1_2=np.nan)


class Footprintable(Classifications):
    """
    this is the object that footprint calculations run on
    """
    portfolio_code: Optional[str] = None

    weight: Optional[float] = None
    nav_nok: Optional[float] = None
    ownership: Optional[float] = None
    attribution: Optional[float] = None

    emis_disclosure_cat: Optional[TrucostDataQuality] = None
    emis_report_year: Optional[float] = np.nan
    data_quality: Optional[str] = None

    fundamental: Optional[float] = None
    emissions: EmissionsScopes = EmissionsScopes._create_empty()
    intensity: EmissionsScopes = EmissionsScopes._create_empty()
    contribution: EmissionsScopes = EmissionsScopes._create_empty()

    trend: Optional[int] = np.nan
