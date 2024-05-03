import logging

import pytest

logger = logging.getLogger(__name__)


def test_true():
    assert 1 == 1


def test_fail():
    assert 43 % 2 == 0



def test_lower():
    assert 'KisKuTYa'.lower() == 'kiskutya'


@pytest.mark.parametrize('a', (0, 2, 4, 6, 7))
def test_even(a):
    assert a % 2 == 0

def add(a, b):
    return a + b

@pytest.mark.parametrize('a, b, c', ((1, 1, 2), (1, 2, 3), (12, 23, 35)))
def test_add(a, b, c):
    logger.debug('Testing: %(a)s + %(b)s == %(c)s', dict(a=a, b=b, c=c))
    assert add(a, b) == c


@pytest.fixture(scope='module')
def fib_nums():
    logger.info('Calculating Fibonacci numbers')
    l = [1, 1]
    while l[-1] < 100:
        l.append(l[-2]+l[-1])
    return l

@pytest.mark.parametrize('a', (1, 2, 3, 5, 8))
def test_fibonacci(a, fib_nums):
    assert a in fib_nums

