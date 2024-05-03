import logging

import pytest

from quadratic_solver import QuadraticSolver


logger = logging.getLogger(__name__)


def test_init():
    s = QuadraticSolver(1, 2, 3)

    assert isinstance(s.a, float)
    assert isinstance(s.b, float)
    assert isinstance(s.c, float)

    assert s.a == 1.0
    assert s.b == 2.0
    assert s.c == 3.0


@pytest.mark.parametrize(
    'a, b, c, x1, x2', (
    (1, 0, -9, 3, -3),
    (1, -2, 0, 2, 0),
    )
)
def test_solver(a, b, c, x1 ,x2):
    s = QuadraticSolver(a, b, c)
    s1, s2 = s.solve()
    assert s1 == x1
    assert s2 == x2
