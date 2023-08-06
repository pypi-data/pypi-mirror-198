"""Test configuration for pytest.

:author: Shay Hill
:created: 2023-03-18
"""


def pytest_assertrepr_compare(config, op, left, right):
    """See full error diffs"""
    if op in ("==", "!="):
        return [f"{left} {op} {right}"]
