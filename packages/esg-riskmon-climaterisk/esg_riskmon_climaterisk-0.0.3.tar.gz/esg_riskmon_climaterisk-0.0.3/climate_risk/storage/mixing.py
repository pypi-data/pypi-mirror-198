import pandas as pd

from datetime import date
from typing import Optional
from entities.const import AllowedTypes
from storage.classifications import Classifications
from storage.compositions import Compositions
from storage.date import DateStorage
from storage.emissions import Emissions
from storage.flexi import FlexiStorage


class CFRetrievePrepare():
    """
    this class' purpose is to create a dataframe that can be used for footprinting
    and other purposes that require the composition, emissions, fundamentals and classifications
    """
    def __init__(self, date: Optional[str] = None) -> None:
        self.date = date

    def _get_emission(
        self, ri_report: bool,
        with_medians: bool,
        cover: pd.DataFrame,
        fk_dim_date: Optional[date] = None,
        year: Optional[int] = None
    ):
        # get trucost data (emissions related and turnover)
        emis_storage = Emissions(
            year=year
        )
        emission_data = emis_storage.get(
            ri_report=ri_report,
            with_medians=with_medians,
            cover=cover, date=fk_dim_date
        )
        return emission_data

    def _get_composition(self, p_type: AllowedTypes, fk_dim_date: date):
        # get portfolio composition
        composition_storage = Compositions(type=p_type)
        portfolio_data = composition_storage.get(
            fields=[],
            as_df=True,
            date=fk_dim_date
        )
        return portfolio_data

    def _get_classification(self, fk_dim_date: date):
        # get classification data to map medians onto
        clas_storage = Classifications()
        classification_data = clas_storage.get(as_df=True, date=fk_dim_date)
        return classification_data

    def _get_fundamental(self, fk_dim_date: date):
        # get portfolio composition
        fundamental_storage = FlexiStorage(
            vendor="fundamentals",
            sql_file="fundamentals.sql"
        )
        fundamental_df = fundamental_storage.get(
            as_df=True,
            date=fk_dim_date
        )
        return fundamental_df

    def create(
        self, ri_report: bool, year: Optional[int],
        with_medians: bool, p_type: AllowedTypes
    ):
        # get fk dim date required
        date_dict = DateStorage().get(date=self.date)
        fk_dim_date = date_dict[0].fk_dim_date
        # get portfolio data
        portfolio_data = self._get_composition(p_type, fk_dim_date=fk_dim_date)
        # get fundamental data
        fundamental_data = self._get_fundamental(fk_dim_date=fk_dim_date)
        # get classification data
        classification_data = self._get_classification(fk_dim_date=fk_dim_date)
        # merge financial and portfolio data to use for sector medians
        proxy_revenue_df = fundamental_data.merge(
            portfolio_data, how="right", left_index=True, right_index=True
        )
        # remove any potential duplicates in revenue data
        proxy_revenue_df = proxy_revenue_df.loc[~proxy_revenue_df.index.duplicated(keep="first")]
        proxy_revenue_df = classification_data.merge(proxy_revenue_df, how="right", left_index=True, right_index=True)

        # pass turnover to assure coverage is met
        p_emissions = self._get_emission(
            ri_report=ri_report,
            with_medians=with_medians,
            year=year,
            cover=proxy_revenue_df,
            fk_dim_date=fk_dim_date
        )
        # merge emissions and portfolio data with fundamentals
        if not with_medians:
            portfolio_data = fundamental_data.merge(portfolio_data, how="right", left_index=True, right_index=True)
        p_emissions = p_emissions.merge(portfolio_data, how="right", left_index=True, right_index=True)
        p_emissions.reset_index(inplace=True)
        return p_emissions
