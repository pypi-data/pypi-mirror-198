"""Simplify a polyline with Visvalingham-Whyatt or Douglas-Peucker.

Visvalingham-Whyatt removes the smallest triangles formed by three consecutive points
in a polyline or polygon. The big advantage for my purposes is that the starting
point on a polygon will not affect the result. The big disadvantage is that tall,
thin spikes are removed along with short, thin triangles. So the smoothed polygon or
polyline may not fit in anything close to the convex hull of the input.

Douglas-Peucker gives a better representation of the convex hull. The big
disadvantage with Douglas-Peucker is that the starting point on a polygon will affect
the result. I've addressed this in the slow, but ideal (for my purposes) `simplify`
function.

:author: Shay Hill
:created: 2022-05-04
"""


from __future__ import annotations

from bisect import insort
from functools import cached_property
from typing import TYPE_CHECKING, Annotated

import numpy as np

from simplify_polyline.helpers import get_line_seg_dists, remsort

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence

    import numpy.typing as npt

    from simplify_polyline.type_hints import Vector, Vertex, Vertices

    _Triangle = Annotated[npt.NDArray[np.float_], (3, 2)]


class Point:
    """A simple double-linked node.

    Knows its prev and next nodes and the area of the triangle formed by itself and
    its prev and next nodes.

    At __init__, initialize self._prev and self._next to None. These None values will
    raise a value error when self.prev and self.none attributes are accessed. In
    order for a Point instance to have an area, you will have to assign a self.next
    and self.prev* after init.

    * self.prev is not directly set-able. self.prev is set when self is set as another
    Point instance's self.next. See method @next.setter for clarification.

    Bypassed nodes are bypassed *after* this node. So if I bypass original nodes 2
    through 5, I will end up with

    Point(0)
    Point(1) in which .bypassed = [2, 3, 4, 5]
    Point(6)
    """

    # constant for use in triangle area calculation
    _ONES_COLUMN = np.array([[1.0], [1.0], [1.0]], dtype=float)

    def __init__(self, vert: Vertex) -> None:
        """Initialize a Point instance."""
        self.vert = np.array(vert)
        self.bypassed: list[Vertex] = []
        self.prev: Point | None = None
        self._next: Point | None = None

    @property
    def next(self) -> Point | None:
        """Get the next node in the linked list."""
        return self._next

    @next.setter
    def next(self, next_point: Point):
        """Set next attribute for self and prev attribute for self.next.

        :param next_point: The next node in the linked list.

        Clear the `doubled_area` property caches because area will change.
        """
        for point in (self, next_point):
            _ = point.__dict__.pop("doubled_area", None)
        self._next = next_point
        next_point.prev = self

    def new_next(self, vert: Vertex) -> Point:
        """Create a new Point instance and set it as self.next.

        :param vert: vert value for new point
        :return: newly created point
        """
        next_point = Point(vert)
        self.next = next_point
        return next_point

    def bypass(self) -> tuple[Point, Point]:
        """Update self.prev and self.next to skip this point.

        :return: the prev and next nodes of the bypassed self

        Bypassed points are cached as vertices, all other info is destroyed.
        """
        if self.prev is None or self.next is None:
            msg = "cannot bypass first or last node in a polyline"
            raise AttributeError(msg)
        prev_point, next_point = self.prev, self.next
        prev_point.next = next_point
        prev_point.bypassed += [self.vert, *self.bypassed]
        return prev_point, next_point

    def restore(self, bypassed_index: int) -> None:
        """Promote a vector in self.bypassed to a Point node."""
        if self.next is None:
            msg = "attempting to restore end point"
            raise AttributeError(msg)
        self_next = self.next
        next_point = self.new_next(self.bypassed[bypassed_index])
        next_point.next = self_next
        self.bypassed, next_point.bypassed = (
            self.bypassed[:bypassed_index],
            self.bypassed[bypassed_index + 1 :],
        )

    @property
    def bypassed_dists(self) -> Vector:
        """The Euclidian distance between each bypassed vert and self -> self.next."""
        if self.next is None:
            msg = "last point in polyline does not bypass any vert"
            raise ValueError(msg)
        return get_line_seg_dists(np.array(self.bypassed), self.vert, self.next.vert)

    @property
    def _triangle(self) -> _Triangle:
        """Triangle made up of prev, self, and next vert values."""
        if self.prev is not None and self.next is not None:
            return np.array([self.prev.vert, self.vert, self.next.vert]).astype(float)
        msg = "first and last point in polyline cannot form a triangle"
        raise AttributeError(msg)

    @cached_property
    def doubled_area(self) -> float:
        """Get twice the area of the triangle formed by, prev - self - next.

        :return: if self.prev and self.next are defined, twice the area of triangle
            (prev.self.next). Otherwise, np.inf.
        """
        try:
            tri_matrix = np.append(self._triangle, type(self)._ONES_COLUMN, axis=1)
        except AttributeError:
            return np.inf
        return abs(np.linalg.det(tri_matrix))

    @property
    def _sorting_key(self) -> tuple[float, int]:
        """Sory by doubled_area, use id as a tiebreaker."""
        return (self.doubled_area, id(self))

    def __lt__(self, other: Point) -> bool:
        """Sort instances by doubled_area.

        In practice, Point instances will be sorted as tuples of (doubled_area, self)
        or (distance_from_segment, self), and ties will be unlikely, but just in
        case, sort by id to avoid an exception in case of a tie in the first tuple
        value.
        """
        return self._sorting_key < other._sorting_key


def _get_few_pts_error_msg(point_llist: PointLList) -> str:
    """Define error message if too few points are provided for a polygon or polyline."""
    if point_llist.min_points == 2:
        return "At least 2 points are required to form a polyline"
    return "At least 3 points are required to form a polygon"


class PointLList:
    """Keep track of the head of the linked list of points."""

    def __init__(self, verts: Vertices, *, is_closed: bool) -> None:
        """Create a linked list of points from a list of vertices.

        :param verts: vertices of the polygon
        :param is_closed: whether the polygon is closed
        """
        self.len = len(verts)
        self.head: Point = Point(verts[0])

        at = self.head
        for vert in verts[1:]:
            at = at.new_next(vert)
        if is_closed:
            at.next = self.head
            self.min_points = 3
        else:
            self.min_points = 2
        if len(verts) < self.min_points:
            raise ValueError(_get_few_pts_error_msg(self))

    def __iter__(self) -> Iterator[Point]:
        """Iterate over the points in the linked list."""
        at: Point | None = self.head
        for _ in range(self.len):
            if at is not None:
                yield at
                at = at.next
            else:
                msg = f"expected {self.len} points, found fewer"
                raise RuntimeError(msg)

    def bypass_point(self, point: Point) -> tuple[Point, Point]:
        """Unlink a point. Move head if necessary.

        :param point: point to unlink
        :return: the previous and next points
        """
        if self.len <= self.min_points:
            raise ValueError(_get_few_pts_error_msg(self))
        if point.prev is None or point.next is None:
            msg = "cannot bypass first or last node in a polyline"
            raise AttributeError(msg)
        if point is self.head:
            self.head = point.next
        self.len -= 1
        return point.bypass()

    def simplify(self, min_area: float) -> None:
        """Bypass points with < min_area triangles.

        Visvalingham-Whyatt algorighm.

        Remove point, prev, and next from queue. Reinsert prev and next (which will
            have new doubled areas).
        """
        queue = sorted(self)
        min_doubled_area = min_area * 2
        while self.len > self.min_points and queue[0].doubled_area < min_doubled_area:
            removed = queue.pop(0)
            assert removed.next is not None
            assert removed.prev is not None
            remsort(queue, removed.prev)
            remsort(queue, removed.next)
            adjacents = self.bypass_point(removed)
            for adjacent in adjacents:
                insort(queue, adjacent)

    def complexify(self, min_dist: float):
        """Add back bypassed points if distance is > min_dist."""
        at = self.head
        while at.next is not None:
            while len(at.bypassed):
                dists = at.bypassed_dists
                if max(dists) < min_dist:
                    break
                self.len += 1
                at.restore(int(np.argmax(dists)))
            at = at.next
            if at is self.head:
                return


def _align_parameters(
    verts: Vertices | Sequence[Vertex] | Sequence[Sequence[float]],
    is_closed: bool | None,
) -> tuple[Vertices, bool]:
    """Adjust parameters for simplification functions.

    :param verts: a sequence two tuples or anything else than can be cast into a
        '*, 2' array.
    :param is_closed: a boolean or None
    :return: a 2-tuple
        0. input `points` with last point removed if the polygon is closed (i.e., if
           the last point is meant to be treated as a copy of the first point). This
           would happen if you specified a pentagon with five unique points, but
           repeated the first point to show that the polygon is closed. Removing the
           redundant copy of the first point simplifies the algorithm as it reduces
           the len of `points` to the number of distinct point instances in the
           polygon. The last, duplicate point will be replaced in the return value.

        2. input `is_closed` if specified, or inferred boolean if not specified.
           If `is_closed` is not specified, is_closed will be set to True if
           points[0] == points[-1] else set to False
    """
    verts_array = np.asarray(verts, dtype=float)
    do_verts_loop = np.array_equal(verts_array[0], verts_array[-1])
    if is_closed is None:
        is_closed = do_verts_loop
    if is_closed and do_verts_loop:
        verts_array = np.array(verts_array[:-1])
    else:
        verts_array = np.array(verts_array)
    return verts_array, is_closed


def vw_simplify(
    verts: Vertices | Sequence[Vertex] | Sequence[Sequence[float]],
    min_area: float = np.inf,
    *,
    is_closed: bool | None = None,
) -> Vertices:
    """Simplify a polyline or polygon using Visvalingham-Whyatt.

    :param verts: vertices along polyline. Anything that can be cast into a '*, 2'
        array.
    :param min_area: minimum triangle area to NOT be culled. Default value of 0 will
        cull all points necessary to return to_point_count.
    :param is_closed: optionally specify whether verts describe a polyline or polygon.
        If not specified, is_closed is inferred from verts[0] == verts[-1]. The form
        of the input (last vert == first vert) will be replicated in the output.
    """
    verts_array, is_closed = _align_parameters(verts, is_closed=is_closed)
    points = PointLList(verts_array, is_closed=is_closed)
    points.simplify(min_area)

    simplified = [x.vert for x in points]
    if np.array_equal(verts[0], verts[-1]):
        simplified += simplified[:1]
    return np.array(simplified, dtype=float)


def simplify(
    verts: Vertices | Sequence[Vertex] | Sequence[Sequence[float]],
    min_dist: float = np.inf,
    *,
    is_closed: bool | None = None,
) -> Vertices:
    """Simplify a polyline or polygon using Douglas-Peucker algorithm.

    :param verts: vertices along polyline. Anything that can be cast into a '*, 2'
        array.
    :param min_dist: minimum height above a line segment for a point to be included.
    :param is_closed: optionally specify whether verts describe a polyline or polygon.
        If not specified, is_closed is inferred from verts[0] == verts[-1]. The form
        of the input (last vert == first vert) will be replicated in the output.

    The downside of the Douglas-Peucker algorithm is that at least two points are
    selected before the algorithm begins. In the case of a polyline, this means that
    the first and last points are always included. In the case of a polygon, this
    means that the first and last points are always included, and the first and last
    points are selected. That works. In the case of a polygon, *any* two points could
    be selected. To avoid this, the Visvalingam-Whyatt algorithm is used to simplify
    the polygon to three points, then Douglas-Peucker is used to add back points
    until the minimum distance is met.
    """
    verts_array, is_closed = _align_parameters(verts, is_closed)
    if is_closed:
        points = PointLList(verts_array, is_closed=True)
        points.simplify(float("inf"))
    else:
        # create a points llist with the first and last points
        endpts = np.array([verts_array[0], verts_array[-1]], dtype=float)
        points = PointLList(endpts, is_closed=False)
        points.head.bypassed = list(verts_array[1:-1])

    points.complexify(min_dist)

    simplified = [x.vert for x in points]
    if np.array_equal(verts[0], verts[-1]):
        simplified += simplified[:1]
    return np.array(simplified, dtype=float)
