from typing import List

import pandas as pd
from entities.const import Const
from scipy.stats import shapiro, yeojohnson


class IQROutliers():
    def __init__(self, data_quality: List[int]) -> None:
        self.data_quality = data_quality
        # TODO: add use of these

    def source(self, emission_data, year):
        # reduce emissions to year
        emission_data = emission_data.loc[emission_data["report_date"].eq(year)]

        # quick calculation of intensity
        emission_data["intensity_1"] = emission_data["emissions_tonnes_s1"] / emission_data["turnover_usd_mln"]
        emission_data["intensity_2"] = emission_data["emissions_tonnes_s2"] / emission_data["turnover_usd_mln"]

        # keep only high quality to understand sample sizes
        p_emissions = emission_data.loc[emission_data["nbim_numerical"].eq(1) | emission_data["nbim_numerical"].eq(2)]
        p_emissions.set_index(Const.ORG_CODE, inplace=True)
        return p_emissions

    def _3_stdev_outliers(self, df):
        # 3 standard deviation limit
        # calculate Q1 and Q3
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        # calculate IQR
        IQR = Q3 - Q1
        # filter dataset with IQR
        IQR_outliers = df[((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
        no_outliers_df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
        return IQR_outliers, no_outliers_df

    def get_sectors_unique(self, p_emissions, icb_level):
        # check count by sector
        count_s = p_emissions.groupby(by=icb_level)["intensity_1"].count()
        # at sector level 1 and sector level 2 there are no sectors with less than 200 records
        # TODO: add warning about sector count

        # take all unique sector level 2
        unique_icbs = p_emissions[icb_level].dropna().unique().tolist()
        return unique_icbs

    def normality_checks(self, p1: float, p2: float, sector: str, use_sc12_sub: pd.DataFrame):
        if p1 >= 1e-3 and p2 >= 1e-3:
            print(f"{sector} scope 1 and 2 intensity is normally distributed")
        elif p1 < 1e-3 and p2 < 1e-3:
            print(f"both {sector} scopes are not normal. transforming.")
            use_sc12_sub["intensity_1"], _ = yeojohnson(use_sc12_sub["intensity_1"])
            use_sc12_sub["intensity_2"], _ = yeojohnson(use_sc12_sub["intensity_2"])
        elif (p1 >= 1e-3 and p2 < 1e-3) or (p1 < 1e-3 and p2 >= 1e-3):
            print(f"!!!! check sector {sector}. scopes are not both equally distributed. transforming separately !!!!")
            if p1 < 1e-3:
                use_sc12_sub["intensity_1"], _ = yeojohnson(use_sc12_sub["intensity_1"])
            if p2 < 1e-3:
                use_sc12_sub["intensity_2"], _ = yeojohnson(use_sc12_sub["intensity_2"])
        return use_sc12_sub

    def sector_outliers(self, icb_level, p_emissions):
        unique_icbs = self.get_sectors_unique(p_emissions, icb_level)

        outliers = {}
        for sector in unique_icbs:
            # subset dataframe to sector level 2
            sl2_subset = p_emissions.loc[p_emissions[icb_level].eq(sector)]
            use_sc12_sub = sl2_subset.copy()

            # check normality
            try:
                _, p1 = shapiro(sl2_subset[["intensity_1"]])
                _, p2 = shapiro(sl2_subset[["intensity_2"]])
            except ValueError:
                print(f"could not calculate symmetry for sector {sector}")
                continue

            # transform if required
            use_sc12_sub = self.normality_checks(p1, p2, sector, use_sc12_sub)

            # calculate outliers here for each sector level 2 as we have enough granularity
            IQR_outliers_sc1, _ = self._3_stdev_outliers(use_sc12_sub[["intensity_1"]])
            IQR_outliers_sc2, _ = self._3_stdev_outliers(use_sc12_sub[["intensity_2"]])

            out = []
            out.extend(IQR_outliers_sc2.index.tolist())
            out.extend(IQR_outliers_sc1.index.tolist())

            # check cleaned up dataset
            cleaned = sl2_subset.loc[~sl2_subset.index.isin(out)]

            # store
            outliers.update({
                sector: out
            })
        return outliers, unique_icbs
