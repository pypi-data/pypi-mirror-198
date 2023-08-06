"""
Infinities
"""
import math


def wr(o):
    if isinstance(o, _Base):
        return o
    if o == math.nan:
        return Nan()
    if o == math.inf:
        return Aleph1()
    if o == -math.inf:
        return Aleph1(False)
    return o


class _Base:
    pass


class Nan(_Base):
    def __repr__(self):
        return 'nan'
    def __eq__(self, o):
        return isinstance(wr(o), Nan)


class Inf(_Base):
    name = 'א‎'
    def __init__(self, positive=True):
        self.positive = positive
    def __repr__(self):
        s = '' if self.positive else '-'
        return s + self.name
    def __hash__(self):
        return hash((self.__class__, self.name, self.positive))
    def __bool__(self):
        return True
    def __neg__(self):
        return type(self)(not self.positive)
    def __radd__(self, o):
        return self + o
    def __rmul__(self, o):
        return self * o


class Aleph0(Inf):
    name = Inf.name + '0'
    def __eq__(self, o):
        o = wr(o)
        return isinstance(o, Aleph0) and self.positive == o.positive
    def __lt__(self, o):
        o = wr(o)
        if isinstance(o, Aleph1):
            return o.positive
        if isinstance(o, Aleph0):
            return self.positive < o.positive
        return not self.positive
    def __le__(self, o):
        o = wr(o)
        if isinstance(o, Aleph1):
            return o.positive
        if isinstance(o, Aleph0):
            return self.positive <= o.positive
        return not self.positive
    def __gt__(self, o):
        o = wr(o)
        if isinstance(o, Aleph1):
            return not o.positive
        if isinstance(o, Aleph0):
            return self.positive > o.positive
        return self.positive
    def __ge__(self, o):
        o = wr(o)
        if isinstance(o, Aleph1):
            return not o.positive
        if isinstance(o, Aleph0):
            return self.positive >= o.positive
        return self.positive
    def  __add__(self, o):
        o = wr(o)
        if isinstance(o, Nan):
            return Nan()
        if isinstance(o, Aleph1):
            return type(o)(o.positive)
        if isinstance(o, Aleph0) and self.positive != o.positive:
            return Nan()
        return type(self)(self.positive)
    def __sub__(self, o):
        o = wr(o)
        if isinstance(o, Nan):
            return Nan()
        if isinstance(o, Aleph1):
            return type(o)(not o.positive)
        if isinstance(o, Aleph0) and self.positive == o.positive:
            return Nan()
        return type(self)(self.positive)
    def __rsub__(self, o):
        o = wr(o)
        if isinstance(o, Nan):
            return Nan()
        if isinstance(o, Aleph1):
            return type(o)(o.positive)
        if isinstance(o, Aleph0) and self.positive == o.positive:
            return Nan()
        return type(self)(not self.positive)
    def __mul__(self, o):
        o = wr(o)
        if isinstance(o, Nan):
            return Nan()
        if isinstance(o, Aleph1):
            return type(o)(self.positive == o.positive)
        if isinstance(o, Aleph0):
            return type(o)(self.positive == o.positive)
        if o == 0:
            return Nan()
        o_positive = o > 0
        return type(self)(self.positive == o_positive)
    def __truediv__(self, o):
        o = wr(o)
        if isinstance(o, _Base) or o == 0:
            return Nan()
        o_positive = o > 0
        return type(self)(self.positive == o_positive)
    def __rtruediv__(self, o):
        o = wr(o)
        if isinstance(o, Aleph1):
            return type(o)(self.positive == o.positive)
        if isinstance(o, Aleph0):
            return Nan()
        return 0


class Aleph1(Inf):
    name = Inf.name + '1'
    def __eq__(self, o):
        o = wr(o)
        return isinstance(o, Aleph1) and self.positive == o.positive
    def __lt__(self, o):
        o = wr(o)
        if isinstance(o, Inf):
            return self.positive < o.positive
        return not self.positive
    def __le__(self, o):
        o = wr(o)
        if isinstance(o, Aleph1):
            return self.positive <= o.positive
        return not self.positive
    def __gt__(self, o):
        o = wr(o)
        if isinstance(o, Aleph1):
            return self.positive > o.positive
        return self.positive
    def __ge__(self, o):
        o = wr(o)
        if isinstance(o, Aleph1):
            return self.positive >= o.positive
        return self.positive
    def __add__(self, o):
        o = wr(o)
        if isinstance(o, Aleph1) and self.positive != o.positive:
            return Nan()
        return type(self)(self.positive)
    def __sub__(self, o):
        o = wr(o)
        if isinstance(o, Aleph1) and self.positive == o.positive:
            return Nan()
        return type(self)(self.positive)
    def __rsub__(self, o):
        o = wr(o)
        if isinstance(o, Aleph1) and self.positive == o.positive:
            return Nan()
        return type(self)(self.positive)
    def __mul__(self, o):
        o = wr(o)
        if o == 0:
            return Nan()
        o_positive = o.positive if isinstance(o, Inf) else o > 0
        return type(self)(self.positive == o_positive)
    def __truediv__(self, o):
        o = wr(o)
        if isinstance(o, _Base) or o == 0:
            return Nan()
        o_positive = o > 0
        return type(self)(self.positive == o_positive)
    def __rtruediv__(self, o):
        o = wr(o)
        if isinstance(o, _Base):
            return Nan()
        return 0


def __getattr__(name):
    if name in ('countable', 'aleph0', 'inf0', 'א‎0'):
        return Aleph0()
    if name in ('uncountable', 'aleph1', 'inf1', 'א‎1'):
        return Aleph1()
    if name in ('nan',):
        return Nan()
    raise AttributeError
