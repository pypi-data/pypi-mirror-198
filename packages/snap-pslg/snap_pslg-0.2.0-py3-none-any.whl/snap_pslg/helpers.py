"""As of right now, one helper function.

:author: Shay Hill
:created: 2023-03-22
"""

from typing import Hashable, TypeVar, Iterable

_HashableT = TypeVar("_HashableT", bound=Hashable)


def get_unique_items(groups: Iterable[Iterable[_HashableT]]) -> set[_HashableT]:
    """Get a set of shared items from a group of iterables.

    :param points: A list of points.
    :return: A set of points.
    """
    union: set[_HashableT] = set()
    for group in groups:
        union |= set(group)
    return union
