import pytest
from esets import eset, inf


A = eset(('a', 'b', 'c'))
B = eset(('d', 'e'))
C = eset(('a', 'd', 'f'))
D = eset(('a', 'b', 'd', 'f'))


def test_cond():
    assert ~A == ~A
    assert A != B
    assert C < D
    assert C <= D
    assert not A < D
    assert not A > D
    assert not A >= D

    assert A < ~eset()
    assert A < ~B
    assert A <= ~B

    assert ~A > B
    assert ~D <= ~C


def test_and():
    assert A & B == set()
    assert A & ~B == A
    assert A & ~C == eset(('b', 'c'))
    assert ~C & A == eset(('b', 'c'))
    assert ~A & ~B == ~eset(('a', 'b', 'c', 'd', 'e'))


def test_or():
    assert A | B == eset(('a', 'b', 'c', 'd', 'e'))
    assert A | ~B == ~eset(['d', 'e'])
    assert A | ~C == ~eset(['d', 'f'])
    assert ~C | A == ~eset(['d', 'f'])
    assert ~A | ~B == ~eset()


def test_sub():
    assert A - B == {'a', 'b', 'c'}
    assert A - ~B == set()
    assert A - ~C == {'a'}
    assert ~A - C == ~eset(['a', 'b', 'c', 'd', 'f'])
    assert ~A - ~D == {'a', 'b'}


def test_updates():
    a = eset(A)
    a |= B
    assert a == A | B


def test_cardinality():
    a = ~A
    assert abs(a) == inf.countable

