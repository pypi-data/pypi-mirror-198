"""Bring public classes into the package namespace.

:author: Shay Hill
:created: 2023-03-18
"""

from simplify_polyline.helpers import get_line_seg_dists
from simplify_polyline.simplifiers import simplify, vw_simplify

__all__ = ["vw_simplify", "simplify", "get_line_seg_dists"]
