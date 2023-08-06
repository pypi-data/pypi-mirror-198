import pytest
from esets import inf


def test_eq():
    assert inf.countable == inf.countable
    assert inf.countable != 0
    assert inf.countable != inf.uncountable


def test_lt():
    assert not inf.countable < 0
    assert -inf.countable < 0
    assert not inf.countable < inf.countable
    assert -inf.countable < inf.countable

    assert not inf.uncountable < 0
    assert -inf.uncountable < 0
    assert -inf.uncountable < inf.uncountable

    assert inf.countable < inf.uncountable
    assert -inf.countable < inf.uncountable
    assert not inf.countable < -inf.uncountable


def test_le():
    assert not inf.countable <= 0
    assert -inf.countable <= 0
    assert inf.countable <= inf.countable
    assert -inf.countable <= inf.countable

    assert not inf.uncountable <= 0
    assert -inf.uncountable <= 0
    assert -inf.uncountable <= inf.uncountable

    assert inf.countable <= inf.uncountable
    assert -inf.countable <= inf.uncountable
    assert not inf.countable <= -inf.uncountable


def test_gt():
    assert inf.countable > 0
    assert not -inf.countable > 0
    assert not inf.countable > inf.countable
    assert not -inf.countable > inf.countable

    assert inf.uncountable > 0
    assert not -inf.uncountable > 0
    assert not -inf.uncountable > inf.uncountable

    assert not inf.countable > inf.uncountable
    assert not -inf.countable > inf.uncountable
    assert inf.countable > -inf.uncountable


def test_ge():
    assert inf.countable >= 0
    assert not -inf.countable >= 0
    assert inf.countable >= inf.countable
    assert not -inf.countable >= inf.countable

    assert inf.uncountable >= 0
    assert not -inf.uncountable >= 0
    assert not -inf.uncountable >= inf.uncountable

    assert not inf.countable >= inf.uncountable
    assert not -inf.countable >= inf.uncountable
    assert inf.countable >= -inf.uncountable


def test_add():
    assert inf.countable + 2 == inf.countable
    assert 2 + inf.countable == inf.countable
    assert inf.countable + inf.countable == inf.countable
    assert inf.countable + inf.uncountable == inf.uncountable
    assert inf.uncountable + inf.countable == inf.uncountable


def test_sub():
    assert inf.countable - 2 == inf.countable
    assert 2 - inf.countable == -inf.countable
    assert inf.countable - inf.countable == inf.nan
    assert inf.countable - inf.uncountable == -inf.uncountable
    assert inf.uncountable - inf.countable == inf.uncountable


def test_mul():
    assert inf.countable * 2 == inf.countable
    assert 2 * inf.countable == inf.countable
    assert inf.countable * inf.countable == inf.countable
    assert inf.countable * inf.uncountable == inf.uncountable
    assert inf.uncountable * inf.countable == inf.uncountable


def test_div():
    assert inf.countable / 2 == inf.countable
    assert 2 / inf.countable == 0
    assert inf.countable / inf.countable == inf.nan
    assert inf.countable / inf.uncountable == inf.nan
    assert inf.uncountable / inf.countable == inf.nan
