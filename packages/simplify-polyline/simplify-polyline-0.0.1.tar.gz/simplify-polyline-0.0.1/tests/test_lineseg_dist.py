"""Test distance between a point and a line segment.

:author: Shay Hill
:created: 2023-03-18
"""

import numpy as np

from simplify_polyline.helpers import get_line_seg_dists

_diag_dist = 2 ** (1 / 2) / 2


class TestGetLinesegDists:
    """Test distance between a point and a line segment."""

    def test_on_line_seg(self):
        # Test a point that is on the line segment.
        points = np.array([[1, 1]])
        lineseg = (np.array([0, 0]), np.array([2, 2]))
        np.testing.assert_allclose(get_line_seg_dists(points, *lineseg), [0])

    def test_on_pnt_a(self):
        # Test a point that is on the line segment.
        points = np.array([[0, 0]])
        lineseg = (np.array([0, 0]), np.array([2, 2]))
        np.testing.assert_allclose(get_line_seg_dists(points, *lineseg), [0])

    def test_on_pnt_b(self):
        # Test a point that is on the line segment.
        points = np.array([[2, 2]])
        lineseg = (np.array([0, 0]), np.array([2, 2]))
        np.testing.assert_allclose(get_line_seg_dists(points, *lineseg), [0])

    def test_off_line_seg_right(self):
        # Test a point that is off the line segment.
        points = np.array([[0, 1]])
        lineseg = (np.array([0, 0]), np.array([2, 2]))
        np.testing.assert_allclose(get_line_seg_dists(points, *lineseg), [_diag_dist])

    def test_off_line_seg_left(self):
        # Test a point that is off the line segment.
        points = np.array([[1, 0]])
        lineseg = (np.array([0, 0]), np.array([2, 2]))
        np.testing.assert_allclose(get_line_seg_dists(points, *lineseg), [_diag_dist])

    def test_on_line_before_seg(self):
        # Test a point that is off the line segment.
        points = np.array([[0, 1]])
        lineseg = (np.array([1, 1]), np.array([2, 2]))
        np.testing.assert_allclose(get_line_seg_dists(points, *lineseg), [1])

    def test_on_line_after_seg(self):
        # Test a point that is off the line segment.
        points = np.array([[2, 1]])
        lineseg = (np.array([0, 0]), np.array([1, 1]))
        np.testing.assert_allclose(get_line_seg_dists(points, *lineseg), [1])
