from typing import List, Optional

import numpy as np
from entities.cafeprod_fields import RRR, TrucostDataQuality

"""
Collection of validators, for now sf_raw_data_models. Can be referred as decorators for pydantic data models
"""


incomparables = ["nan", "None", None, np.nan]


def normalise(v: Optional[List[str]]):
    if v is None or not v:
        return []
    if isinstance(v, (float, int)):
        return []
    if isinstance(v, list):
        return v
    if len(v.split(", ")) > 1:
        return v.split(", ")
    return [v]


def validate_make_millions(v):
    """
    transforming mcap to millions
    """
    try:
        v = v / 1e6
        return v
    except Exception:
        return 0


def validate_year(v):
    if v in incomparables:
        return np.nan
    elif isinstance(v, str):
        return float(v.replace(",", ""))
    elif isinstance(v, (int, float)):
        return float(v)
    return np.nan


def validate_sign(v):
    if v in incomparables:
        return np.nan
    elif isinstance(v, str):
        v = float(v.replace(",", ""))
    elif isinstance(v, (int, float)):
        v = float(v)
    if v < 0:
        raise Exception
    return v


def validate_tds(v):
    if v in incomparables:
        return TrucostDataQuality.UNKNOWN
    return v


def clean_msci(v):
    if v in incomparables:
        return v
    try:
        new_val = float(v)
    except Exception:
        new_val = v.split(", ")[-1]
    return new_val


def clean_RRR(v):
    if v in incomparables:
        return v
    if v not in RRR.to_list():
        return v.split(", ")[-1]
    return v


def validate_sectors(v: str):
    if v is None or not v or v == "":
        return "Undefined"
    elif not isinstance(v, str):
        return "Undefined"
    return v.strip()


def validate_float(v: float):
    if v in incomparables:
        return np.nan
    elif isinstance(v, str):
        return float(v)
    return v
