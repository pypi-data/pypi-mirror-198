#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning a dict of int/int/int with this signature: CMD [opt] [opt]."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0x85e6b7c83522fe595795ddc7d0cb4525

from pipython import PIDebug

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'qHDT',
    'qHIB',
    'qHIL',
    'qJBS',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_get_noargs(gcs, cmd):
    """No arguments. Will return converted "items". """
    PIDebug('enter test_get_2arg_[opt]_[opt]__{int_{int_int}}.test_get_noargs(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '1 2=3 \n4 5=6 \n7 8=9\n')
    assert OrderedDict([(1, OrderedDict([(2, 3)])), (4, OrderedDict([(5, 6)])),
                        (7, OrderedDict([(8, 9)]))]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_2arg_[opt]_[opt]__{int_{int_int}}.test_wrong_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, ['1', 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, {1: 2})
    checksvr(gcs)


def test_get_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_get_2arg_[opt]_[opt]__{int_{int_int}}.test_get_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1'), '1 2=3\n')
    gcs.svr.queue(cmdstr(cmd, '1'), '1 2=3\n')
    assert OrderedDict([('1', OrderedDict([(2, 3)]))]) == getattr(gcs, cmd)('1')
    assert OrderedDict([(1, OrderedDict([(2, 3)]))]) == getattr(gcs, cmd)(1)
    gcs.svr.queue(cmdstr(cmd, '1 2'), '1 2=3\n')
    gcs.svr.queue(cmdstr(cmd, '1 2'), '1 2=3\n')
    assert OrderedDict([('1', OrderedDict([('2', 3)]))]) == getattr(gcs, cmd)('1', '2')
    assert OrderedDict([(1, OrderedDict([(2, 3)]))]) == getattr(gcs, cmd)(1, 2)
    checksvr(gcs)


def test_get_list_args(gcs, cmd):
    """Arguments as list."""
    PIDebug('enter test_get_2arg_[opt]_[opt]__{int_{int_int}}.test_get_list_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2'), '1 2=3\n')
    gcs.svr.queue(cmdstr(cmd, '1 2'), '1 2=3\n')
    assert OrderedDict([('1', OrderedDict([(2, 3)]))]) == getattr(gcs, cmd)(['1'], [2])
    assert OrderedDict([(1, OrderedDict([('2', 3)]))]) == getattr(gcs, cmd)([1], ['2'])
    gcs.svr.queue(cmdstr(cmd, '1 2 4 5'), '1 2=3 \n4 5=6\n')
    gcs.svr.queue(cmdstr(cmd, '1 2 4 5'), '1 2=3 \n4 5=6\n')
    assert OrderedDict([('1', OrderedDict([(2, 3)])), (4, OrderedDict([('5', 6)]))]) == getattr(gcs, cmd)(['1', 4],
                                                                                                          [2, '5'])
    assert OrderedDict([(1, OrderedDict([('2', 3)])), ('4', OrderedDict([(5, 6)]))]) == getattr(gcs, cmd)([1, '4'],
                                                                                                          ['2', 5])
    checksvr(gcs)


def test_get_answer_with_spaces(gcs, cmd):
    """Controller sends answer with too many spaces."""
    PIDebug('enter test_get_2arg_[opt]_[opt]__{int_{int_int}}.test_get_answer_with_spaces(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '  1\t2 =  3   \n 4   5\t=    6    \n  7    8  =         9\n')
    assert OrderedDict([(1, OrderedDict([(2, 3)])), (4, OrderedDict([(5, 6)])),
                        (7, OrderedDict([(8, 9)]))]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_answer(gcs, cmd):
    """Controller sends wrong answer."""
    PIDebug('enter test_get_2arg_[opt]_[opt]__{int_{int_int}}.test_wrong_answer(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '1 2.5=1\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd), '1.5 2=1\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd), '1 2=1.5\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
