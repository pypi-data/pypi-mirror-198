import numpy as np

from collections import defaultdict
from typing import List, Optional
from entities.calculation_models import Footprintable
from entities.const import Scopes
from climate_risk.errors import ServiceError
from climate_risk.utils import sort_nested


class FootprintAggregator():
    """
    This class calcualtes the footprint for each company and then aggregates it
    TODO: actually the portfolio is just another group (the total group) so change this to reduce code
    TODO: error catching!
    """
    def __init__(self) -> None:
        pass

    def get_grouped(self, data: List, groupby_field: str):
        grouped = defaultdict(list)
        for cmp in data:
            field_name = getattr(cmp, groupby_field)
            try:
                field_name = field_name.value if not isinstance(
                    field_name, (str, float, int)
                ) else field_name
            except AttributeError:
                print(f"Warning: issue with grouping for {field_name}.")
                pass

            try:
                grouped[field_name].append(cmp)
            except AttributeError:
                raise ServiceError(f"Issue grouping fields for {field_name}.")
        return grouped

    def aggregate_group_scopes(
        self,
        groupby_field: str = "carbon_disclosure",
        footprintables: List[Footprintable] = [],
        # this can be emissions, intensity or contribution aggregation
        field: Optional[str] = "contribution",
        keep_top: Optional[int] = None
    ):
        """
        group wide figures for selected grouping field, by scope and for selected method and attribution
        """
        gr = self.get_grouped(footprintables, groupby_field)

        def _get_sum(scope):
            grp_sum = {}
            for grp, companies in gr.items():
                to_sum = []
                for c in companies:
                    v = getattr(getattr(c, field), scope, np.nan)
                    if not isinstance(v, (float, int)):
                        v = np.nan
                    to_sum.append(v)
                grp_sum[grp] = round(np.nansum(to_sum), 2)
            return grp_sum

        req_group_foot = {
            scope: _get_sum(scope)
            for scope in Scopes.to_list()
        }

        sorted_gr_foot = sort_nested(
            req_group_foot, by_key=None, keep_top=keep_top
        )
        return sorted_gr_foot, gr

    def aggregate_portfolio(
        self,
        footprinted_portfolio: List[Footprintable] = []
    ):
        """
        portfolio wide figures by scope (1,2,3) for selected method, attribution and list of companies
        """
        collect_scopes = {}
        for scope in Scopes.to_list():
            collect_scopes[scope] = np.nansum([
                getattr(c.contribution, scope, 0)
                for c in footprinted_portfolio
            ])
        return collect_scopes
