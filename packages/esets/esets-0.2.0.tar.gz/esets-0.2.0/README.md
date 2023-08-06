# eset
Extended sets - support for set complement

## Overview

An `eset` works like a normal python `set` except that you can invert it to generate its
complement.  For example, let's say you have the following:

```
>>> from esets import eset
>>> s = eset(['hello', 'there'])
>>> s_invert = ~s
>>> s_invert
~eset(['hello', 'there'])
```

In this example, `s_invert` contains everything _except_ `'hello'` and `'there'`.

## Logic

All the logic operations you'd expect from sets are available in esets, including
intersection, union, difference, and symmetric difference.  Use the `&`, `|`, `-`, and `^`
operators respectively.

Similarly, conditional expressions are available to determine subset relationships.
If `A <= B`, that A is a subset of B.

### Infinities

You'll note there's an `inf.py` module that implement `א‎0` and `א‎1` infinities, that
is, countable and uncountable infinities. This was implemented so that cardinality
calculations would be correct for complement sets: discussed below.

```
>>> from esets import inf
>>> inf.countable, inf.uncountable
(א‎0, א‎1)
>>> inf.countable < inf.uncountable
True
```

### Cardinality

The `abs` expression (also `cardinality` method) will return a countably infinite scalar
if in complement mode; otherwise it returns the count of items in set.

```
>>> from esets import eset, inf
>>> s = eset(['hello', 'there'])
>>> abs(s)
2
>>> abs(~s)
א‎0
```
