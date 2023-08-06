import pandas as pd

from typing import List, Optional
from entities.cafeprod_fields import TrucostDataQuality


class EmissionComparison():
    """
    this class has methods that aid with classify data and calculate percentage differences between pairs of emissions
    and share of total data above a defined threshold of accepted level of differences
    """
    def __init__(self) -> None:
        pass

    def get_group(
        self,
        df: pd.DataFrame,
        bm_disc: List[TrucostDataQuality],
        vd_disc: List[TrucostDataQuality],
        vd_field: str,
    ):
        """
        This method returns the subset group based on disclosure categories that must have been
        standadised beforehand
        """
        group_subset = df.loc[
            df['trucost_emission_data_source'].isin(bm_disc) &
            df[vd_field].isin(vd_disc)
        ]
        return group_subset

    def calc_pct_diff(
        self, group_subset: pd.DataFrame,
        scope: str
    ):
        """
        this method requires to be passed a dataframe for a group (see get_group)
        it returns the calculated percentage difference for each pairwise comparison between vendors
        """
        # calculate mean
        group_subset[f"{scope}_mean"] = (group_subset[f"emission_{scope}"] + group_subset[scope]) / 2

        # calculate absolute difference
        group_subset[f"{scope}_abs_diff"] = abs((group_subset[f"emission_{scope}"] - group_subset[scope]))

        # calculate percentage difference
        group_subset[f"{scope}_pct_diff"] = round(
            (group_subset[f"{scope}_abs_diff"] / group_subset[f"{scope}_mean"])
            * 100, 2
        )
        return group_subset

    def calc_acceptance_overshoot(
        self,
        df: pd.DataFrame,
        fields: List[str],
        threshold: Optional[float] = 10
    ):
        """
        for a list of fields to filter by defined threshold (in percentage)
        it returns the share of the total data above the threshold for each field
        """
        return {
            field: (df[(df[field] > threshold)].count()[field] / len(df)) * 100
            for field in fields
        }
