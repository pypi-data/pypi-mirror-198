import numpy as np
import pandas as pd
from typing import Any, Dict, Optional, OrderedDict
from operator import itemgetter


def model_to_df(list_obj):
    final = []
    for i in list_obj:
        new_i = {}
        for key, item in i.dict().items():
            if isinstance(item, dict):
                for n_k, n_i in item.items():
                    new_i.update({f"{key}_{n_k}": n_i})
            else:
                new_i.update({key: item})
        final.append(new_i)
    return pd.DataFrame(final)


def aggregate_groups(
    grouped_obj: Dict[str, Any] = {},
    # this can be any flat field
    field: Optional[str] = "contribution"
):
    """
    group wide figures for selected grouping field, by scope and for selected method and attribution
    """
    grp_sum = {}
    for grp, companies in grouped_obj.items():
        grp_sum[grp] = round(np.nanmean([
            c[field]
            for c in companies]
        ), 2)
    return grp_sum


def sort_nested(
    dictionary: Dict,
    by_key: str = None,
    keep_top: Optional[int] = None
):
    # sorts a nested dictionary by nested value that is ORDERED and stored this way
    if by_key:
        return OrderedDict(sorted(dictionary.items(), key=lambda tup: (tup[1][by_key]), reverse=True))

    new_dictionary = {}
    for k, v in dictionary.items():
        ordered = OrderedDict(sorted(v.items(), key=itemgetter(1), reverse=True))
        if keep_top:
            tops = dict(list(ordered.items())[:keep_top])
        else:
            tops = dict(list(ordered.items()))
        new_dictionary.update({k: tops})
    return new_dictionary
