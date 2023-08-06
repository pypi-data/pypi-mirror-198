"""Test visvalingham-whyatt simplification.

:author: Shay Hill
:created: 2023-03-18
"""

import numpy as np

from simplify_polyline.simplifiers import simplify, vw_simplify


class TestVW:
    """Test visvalingham-whyatt simplification."""

    def test_near_linear(self):
        """Linear and near-linear points are removed."""
        points = [(0, 0), (1, 0), (2, 0), (3, 0.01), (4, 0)]
        np.testing.assert_equal(vw_simplify(points, 1), [(0, 0), (4, 0)])

    def test_spike(self):
        """Linear and near-linear points are removed."""
        points = [(0, 0), (1, 0), (1, 1), (2, 2), (0.99, 1), (0, 1)]
        np.testing.assert_equal(
            vw_simplify(points, 0.1), [(0, 0), (1, 0), (1, 1), (0, 1)]
        )

    def test_area(self):
        """Area calculation is correct."""
        points = [(0, 0), (1, 0), (1, 1)]
        true_area = 1 / 2
        slightly_less_than_true_area = true_area - 0.01
        slightly_more_than_true_area = true_area + 0.01
        np.testing.assert_equal(
            vw_simplify(points, slightly_more_than_true_area), [(0, 0), (1, 1)]
        )
        np.testing.assert_equal(
            vw_simplify(points, slightly_less_than_true_area), [(0, 0), (1, 0), (1, 1)]
        )

    def test_closes(self):
        """Simplification closes the path."""
        points = [(0, 0), (1, 0), (1, 1), (0, 0)]
        np.testing.assert_equal(
            vw_simplify(points, 0), [(0, 0), (1, 0), (1, 1), (0, 0)]
        )


class TestDP:
    """Test Douglas-Peucker simplification."""

    def test_near_linear(self):
        """Linear and near-linear points are removed."""
        points = [(0, 0), (1, 0), (2, 0), (3, 0.01), (4, 0)]
        np.testing.assert_equal(simplify(points, 1), [(0, 0), (4, 0)])

    def test_polyline_spike(self):
        """Spikes are retained in polylines."""
        points = [(0, 0), (1, 0), (1, 1), (2, 2), (0.99, 1), (0, 1)]
        np.testing.assert_equal(simplify(points, 0.1), points)

    def test_polygon_spike(self):
        """Spikes are retained in polygons."""
        points = [(0, 0), (1, 0), (1, 1), (2, 2), (0.99, 1), (0, 1), (0, 0)]
        np.testing.assert_equal(simplify(points, 0.1), points)
