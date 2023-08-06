"""Small helper functions.

:author: Shay Hill
:created: 2022-05-12
"""

from __future__ import annotations

import bisect
from typing import TYPE_CHECKING, Protocol, TypeVar

import numpy as np

if TYPE_CHECKING: 
    from simplify_polyline.type_hints import Vector, Vertex, Vertices

_T = TypeVar("_T")


class Comparable(Protocol):
    """Protocol for annotating comparable types."""

    def __lt__(self: _T, other: _T) -> bool:
        ...


_ComparableT = TypeVar("_ComparableT", bound=Comparable)


def remsort(sorted_list: list[_ComparableT], value: _ComparableT) -> None:
    """Remove a value from a sorted list in place.

    This is the inverse of bisect.insort
    """
    index = bisect.bisect_left(sorted_list, value)
    del sorted_list[index]


def get_line_seg_dists(points: Vertices, seg_a: Vertex, seg_b: Vertex) -> Vector:
    """Calculate the Euclidean distance between an array of points to a line segment.

    :param pnt: a point in 2d space
    :param seg_a: beginning of line segment in 2d space
    :param seg_b: end of line segment in 2d space
    :return: a distance from p to segment ab for each p

    by [meowgoesthedog](https://stackoverflow.com/users/10265365/meowgoesthedog)

    https://stackoverflow.com/questions/54442057/calculate-the-euclidian-distance-
    between-an-array-of-points-to-a-line-segment-in
    """
    # Handle case where p is a single point, i.e. 1d array.
    points = np.atleast_2d(points)

    if np.all(seg_a == seg_b):
        return np.linalg.norm(points - seg_a, axis=1)

    # normalized tangent vector
    d = np.divide(seg_b - seg_a, np.linalg.norm(seg_b - seg_a))

    # signed parallel distance components
    s = np.dot(seg_a - points, d)
    t = np.dot(points - seg_b, d)

    # clamped parallel distance
    h = np.maximum.reduce([s, t, np.zeros(len(points))])

    # perpendicular distance component
    c = np.cross(points - seg_a, d)

    # use hypot for Pythagoras to improve accuracy
    return np.hypot(h, c)
