import numpy as np
import pandas as pd
from entities.const import Const

"""
EXTRACT SUSPISCIOUS COMPANIES
- DEFINED AS CHANGES IN INTENSITY >= 200% (DOUBLING) YEAR TO YEAR AND DATA QUALITY STAYING STABLE
"""


class YoYOutliers():
    def __init__(self) -> None:
        self.constituents_df = None
        self.emission_data = None
        self.run_fields = {
            "intensity": ["intensity_1", "intensity_2"],
            "emissions": ["emissions_tonnes_s1", "emissions_tonnes_s2"]
        }
        self.year = None
        self.prev_y = None

    def source(self, emission_data, year):
        self.year = year
        self.prev_y = self.year - 1
        self.emission_data = emission_data
        self.emission_data.reset_index(inplace=True)

        # quick calc of intensity
        self.emission_data["intensity_1"] = self.emission_data["emissions_tonnes_s1"] / self.emission_data["turnover_usd_mln"]
        self.emission_data["intensity_2"] = self.emission_data["emissions_tonnes_s2"] / self.emission_data["turnover_usd_mln"]
        return self.emission_data

    def calc_quality_trend(self, constituents_df):
        # GET CHANGES IN DATA QUALITY, filling unknown quality with category 5
        quality_yearly = pd.pivot_table(
                constituents_df[[Const.ORG_CODE, "report_date", "nbim_numerical"]],
                index=Const.ORG_CODE, columns="report_date", values="nbim_numerical", fill_value=5
            )
        quality_yearly.reset_index(inplace=True)
        # if the quality change is 0 - unchanged, <0 it has improved, >0 got worse
        quality_yearly["quality_change"] = quality_yearly[self.year] - quality_yearly[self.prev_y]
        return quality_yearly

    def _reduce(self, constituents_df, quality_yearly, fields, high_change):
        # reduce to 2021
        constituents_df = constituents_df.loc[constituents_df["report_date"].eq(self.year)]

        # add data quality
        constituents_df = constituents_df.merge(
            quality_yearly[[Const.ORG_CODE, "quality_change"]], how="left",
            right_on=Const.ORG_CODE, left_on=Const.ORG_CODE
        )

        # keep only constituents that are flagged as high change in emissions/intensity
        keep = [Const.ORG_CODE, "nbim_numerical", "report_date", "quality_change"]
        keep.extend(fields)
        tmp = constituents_df[
            keep
        ].loc[constituents_df[Const.ORG_CODE].isin(high_change)]

        # keep only constituents that are flagged as quality not changed from 2020-2021 amongst the high change ones
        no_quality_change = tmp[
            keep
        ].loc[tmp["quality_change"].eq(0)]
        return no_quality_change

    def get_yoy_flag(self, emission_data):
        quality_yearly = self.calc_quality_trend(emission_data)

        flagged = {}
        for k, fields in self.run_fields.items():
            s = {}
            for scope in fields:
                scope_yearly = pd.pivot_table(
                    emission_data[[Const.ORG_CODE, "report_date", scope]],
                    index=Const.ORG_CODE, columns="report_date", values=scope, fill_value=np.nan
                )
                # calculate trend 2020-2021
                scope_yearly["trend"] = abs(((scope_yearly[self.year] - scope_yearly[self.prev_y]) / scope_yearly[self.prev_y])) * 100

                # find yearly changes that are doubled or more yty
                large_changes = scope_yearly.loc[scope_yearly["trend"] >= 100]
                s.update({scope: large_changes[["trend"]]})

            # this is the list of constituents that have high change in either scope 1 or scope 2 intensity or emissions
            high_change: list = []
            high_change.extend(s[fields[0]].index.tolist())
            high_change.extend(s[fields[1]].index.tolist())

            # reduce to 2021 + no change in quality
            no_quality_change = self._reduce(emission_data, quality_yearly, fields, high_change)
            flagged.update({k: no_quality_change[Const.ORG_CODE].tolist()})

        intersection_flagged = list(set(flagged["intensity"]).intersection(flagged["emissions"]))
        print(f"!!! very suspicious candidates intersection of emissions and intensity - {len(list(set(intersection_flagged)))} !!!")
        return flagged
