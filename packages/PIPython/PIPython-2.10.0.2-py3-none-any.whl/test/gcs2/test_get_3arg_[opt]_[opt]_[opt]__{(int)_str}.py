#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning a dict of int/int/str with this signature: CMD [opt] [opt]."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103

__signature__ = 0xdf4ef7cdd48525e9ac87bf1dea595886

from pipython import PIDebug

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'qHIS',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_get_noargs(gcs, cmd):
    """No arguments. Will return converted "items". """
    PIDebug('enter test_get_3arg_[opt]_[opt]_[opt]__{(int)_str}.test_get_noargs(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '2 1 2=08 \n2 3 4=USB Optical Mouse \n3 6 1=0\n')
    assert OrderedDict([((2, 1, 2), '08'), ((2, 3, 4), 'USB Optical Mouse'),
                        ((3, 6, 1), '0')]) == getattr(gcs, cmd)()
    checksvr(gcs)


def Xtest_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_3arg_[opt]_[opt]_[opt]__{(int)_str}.test_wrong_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [1, 2], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [1], [1, 2])
    checksvr(gcs)


def test_get_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_get_3arg_[opt]_[opt]_[opt]__{(int)_str}.test_get_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '2 1 2'), '2 1 2=08\n')
    gcs.svr.queue(cmdstr(cmd, '2 1 2'), '2 1 2=08\n')
    assert OrderedDict([((2, 1, 2), '08')]) == getattr(gcs, cmd)(2, 1, 2)
    assert OrderedDict([((2, 1, 2), '08')]) == getattr(gcs, cmd)('2', '1', '2')
    checksvr(gcs)


def test_get_list_args(gcs, cmd):
    """Arguments as list."""
    PIDebug('enter test_get_3arg_[opt]_[opt]_[opt]__{(int)_str}.test_get_list_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '2 1 2 2 3 4 3 6 1'), '2 1 2=08 \n2 3 4=USB Optical Mouse \n3 6 1=0\n')
    gcs.svr.queue(cmdstr(cmd, '2 1 2 2 3 4 3 6 1'), '2 1 2=08 \n2 3 4=USB Optical Mouse \n3 6 1=0\n')
    assert OrderedDict([((2, 1, 2), '08'), ((2, 3, 4), 'USB Optical Mouse'),
                        ((3, 6, 1), '0')]) == getattr(gcs, cmd)([2, 2, 3], [1, 3, 6], [2, 4, 1])
    assert OrderedDict([((2, 1, 2), '08'), ((2, 3, 4), 'USB Optical Mouse'),
                        ((3, 6, 1), '0')]) == getattr(gcs, cmd)([2, '2', 3], ['1', 3, 6], [2, 4, '1'])
    checksvr(gcs)


def test_get_answer_with_spaces(gcs, cmd):
    """Controller sends answer with too many spaces."""
    PIDebug('enter test_get_3arg_[opt]_[opt]_[opt]__{(int)_str}.test_get_answer_with_spaces(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '2 1  2 =  08 \n  2  3  4  = USB Optical Mouse \n  3   6  1 =0\n')
    assert OrderedDict([((2, 1, 2), '08'), ((2, 3, 4), 'USB Optical Mouse'),
                        ((3, 6, 1), '0')]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_answer(gcs, cmd):
    """Controller sends wrong answer."""
    PIDebug('enter test_get_3arg_[opt]_[opt]_[opt]__{(int)_str}.test_wrong_answer(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '1 2 2.5=1\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd), '1 2.5 2=1\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd), '1.5 2 2=1\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd), '1=1\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd), '1\n')
    with pytest.raises(IndexError):
        getattr(gcs, cmd)()
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
