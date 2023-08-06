#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test helper functios of gcscommands."""
__signature__ = 0xe791ad3f7b144826286c1eba5764ffb0

from pipython import PIDebug

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

from pipython.pidevice.gcs2.gcs2commands import converttonumber, getbitcodeditems


def test_getbitcodeditems():
    """Test function getbitcodeditems()."""
    PIDebug('enter test_helperfunctions.test_getbitcodeditems')
    allitems = ['a', 'B', 'C', 2, 'e', 'f']
    value = 57  # 100111
    items = ['B', 2, 'f']
    assert OrderedDict(
        zip(range(1, 7), [True, False, False, True, True, True])) == getbitcodeditems(value)
    assert OrderedDict(zip(allitems, [True, False, False, True, True, True])) == getbitcodeditems(
        value, allitems)
    assert OrderedDict(zip(items, [False, True, True])) == getbitcodeditems(value, allitems, items)


def test_converttonumber():
    """Test function converttonumber()."""
    PIDebug('enter test_helperfunctions.test_converttonumber')
    assert 45054 == converttonumber('0xaffe')
    assert 127776 == converttonumber('127776')
    assert 17.3 == converttonumber('17.3')
    assert '17,3' == converttonumber('17,3')
    assert '17.3a' == converttonumber('17.3a')


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
