import numpy as np

from typing import List
from entities.cafeprod_fields import PCAFSectors
from entities.calculation_models import (EmissionsScopes, Footprintable)
from entities.const import Const
from entities.sf_raw_data_models import PortCompanyFootprintData
from services.footprint_exec import OE, TCE, WACI


class GenericFootprintProtocol():
    def __init__(
        self,
        method: str, attribution: str,
        companies: List[PortCompanyFootprintData] = []
    ):
        # 0. set attribution field
        self.attribution = attribution

        # 1. which footprinting methodology do we need to follow
        footprint_method_map = {
            Const.WACI: WACI,
            Const.TCE: TCE,
            Const.OE: OE
        }
        self.execute_methodology = footprint_method_map[method]

        # 2. make footprint
        self.footprinted = self._make_footprint(companies)

    def _set_weights(
        self, foot: Footprintable,
        cmp: PortCompanyFootprintData
    ):
        # assign weights
        foot.weight = cmp.pf_weight
        # set outstanding amount
        foot.nav_nok = cmp.nav_nok
        return foot

    def _set_emissions(self, foot: Footprintable, cmp: PortCompanyFootprintData):
        # no standard yet
        pass

    def _make_footprint(self, companies: List[PortCompanyFootprintData] = []):
        footprinted_portfolio = []
        for cmp in companies:
            foot = Footprintable(**cmp.dict())
            # set weights
            foot = self._set_weights(foot, cmp)
            # move over data quality info
            foot.data_quality = cmp.data_quality
            # set ownership; this is consistent with previous years
            foot.ownership = cmp.ownership
            # set emissions to use
            foot = self._set_emissions(foot, cmp)
            # set fundamental to use
            foot.fundamental = getattr(cmp, self.attribution)
            # decide which method of contribution to calculate and execute
            self.execute_methodology(foot).contribution()
            footprinted_portfolio.append(foot)
        return footprinted_portfolio


class CustomProtocol(GenericFootprintProtocol):
    """
    this is the custom footprinting footprint_protocol
    any methodology is allowed
    """
    def __init__(
        self,
        method: str = Const.WACI,
        attribution: str = Const.REV,
        companies: List[PortCompanyFootprintData] = []
    ) -> None:
        super().__init__(method, attribution, companies)

    def _set_emissions(self, foot: Footprintable, cmp: PortCompanyFootprintData):
        # deciding which scope 3 should be included
        scope_3 = None
        # setting emissions
        foot.emissions = EmissionsScopes(
            scope_1=cmp.emissions_tonnes_s1,
            scope_2=cmp.emissions_tonnes_s2,
            scope_3=scope_3,
            scope_1_2=cmp.emissions_tonnes_s12
        )

        foot.intensity = EmissionsScopes(
            scope_1=cmp.proxy_median_intensity_s1,
            scope_2=cmp.proxy_median_intensity_s2,
            scope_3=scope_3,
            scope_1_2=np.nansum([cmp.proxy_median_intensity_s1, cmp.proxy_median_intensity_s2])
        )
        # setting disclosure category and reporting year
        foot.emis_disclosure_cat = cmp.carbon_disclosure
        foot.emis_report_year = cmp.report_date
        return foot


class PCAFProtocol(GenericFootprintProtocol):
    """
    for now the only difference is which scope 3 sectors we are including
    only PCAF consistent methods are allowed to set emissions, attribution etc.
    NOTE: not implemented yet & not tested
    """
    def __init__(
        self, method: str = Const.WACI,
        attribution: str = Const.REV,
        companies: List[Footprintable] = []
    ) -> None:
        super().__init__(method, attribution, companies)

    def _set_emissions(self, foot: Footprintable, cmp: PortCompanyFootprintData):
        """
        this decides which inference type to use
        it also decides whether to include scope 3 etc.
        or which categories to include at all
        """
        # TODO: change this, this field needs to come from the db
        # deciding which scope 3 should be included
        scope_3 = None
        if cmp.industry_level_1 not in PCAFSectors.to_list():
            scope_3 = 0
        # setting emissions
        foot.emissions = EmissionsScopes(
            scope_1=cmp.emissions_tonnes_s1,
            scope_2=cmp.emissions_tonnes_s2,
            scope_3=scope_3,
            scope_1_2=cmp.emissions_tonnes_s12
        )

        foot.intensity = EmissionsScopes(
            scope_1=cmp.proxy_median_intensity_s1,
            scope_2=cmp.proxy_median_intensity_s2,
            scope_3=scope_3,
            scope_1_2=np.nansum([cmp.proxy_median_intensity_s1, cmp.proxy_median_intensity_s2])
        )
        # setting disclosure category and reporting year
        foot.emis_disclosure_cat = cmp.carbon_disclosure
        foot.emis_report_year = cmp.report_date
        return foot
