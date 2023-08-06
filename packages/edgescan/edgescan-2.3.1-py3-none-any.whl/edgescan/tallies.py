import collections
from typing import Dict, Iterable, Union

import edgescan.types


def tally_by(rows: Iterable[dict], selector: Union[str, callable]) -> Dict[str, int]:
    if isinstance(selector, str):
        k = selector
        f = lambda o: o[k]
    elif callable(selector):
        f = selector
    else:
        raise TypeError(f"selector must be a string or callable, not {type(selector)}")

    tally = collections.defaultdict(int)
    for row in rows:
        v = f(row)
        if v is not None:
            try:
                if isinstance(v, str) is False and edgescan.types.is_iterable(v):
                    for item in v:
                        if item is not None:
                            tally[item] += 1
                else:
                    tally[v] += 1
            except KeyError:
                continue

    return dict(tally)


def sort_by_key(tally: dict, descending: bool = False) -> collections.OrderedDict:
    return collections.OrderedDict(sorted(tally.items(), key=lambda x: x[0], reverse=descending))


def sort_by_value(tally: dict, descending: bool = True) -> collections.OrderedDict:
    return collections.OrderedDict(sorted(tally.items(), key=lambda x: x[1], reverse=descending))
