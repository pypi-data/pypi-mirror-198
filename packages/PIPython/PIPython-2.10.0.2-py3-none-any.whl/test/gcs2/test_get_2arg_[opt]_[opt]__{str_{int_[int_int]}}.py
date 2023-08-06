#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning a dict of str/int/int_int with this signature: CMD [opt] [opt]."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0xed1d5b4bec89f7a2faa5ca3a18d63689

from pipython import PIDebug

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'qHIA',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_get_noargs(gcs, cmd):
    """No arguments. Will return converted "items". """
    PIDebug('enter test_get_2arg_[opt]_[opt]__{str_{int_[int_int]}}.test_get_noargs(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '1 2=11 12 \n4 5=14 15 \n7 8=17 18\n')
    assert OrderedDict([('1', OrderedDict([(2, [11, 12])])), ('4', OrderedDict([(5, [14, 15])])),
                        ('7', OrderedDict([(8, [17, 18])]))]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_2arg_[opt]_[opt]__{str_{int_[int_int]}}.test_wrong_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, ['1', 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, {1: 2})
    checksvr(gcs)


def test_get_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_get_2arg_[opt]_[opt]__{str_{int_[int_int]}}.test_get_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2'), '1 2=11 12\n')
    assert OrderedDict([('1', OrderedDict([(2, [11, 12])]))]) == getattr(gcs, cmd)('1', 2)
    gcs.svr.queue(cmdstr(cmd, '1 2'), '1 2=11 12\n')
    assert OrderedDict([(1, OrderedDict([(2, [11, 12])]))]) == getattr(gcs, cmd)(1, '2')
    checksvr(gcs)


def test_get_list_args(gcs, cmd):
    """Arguments as list."""
    PIDebug('enter test_get_2arg_[opt]_[opt]__{str_{int_[int_int]}}.test_get_list_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 4 5 7 8'), '1 2=11 12 \n4 5=14 15 \n7 8=17 18\n')
    assert OrderedDict([('1', OrderedDict([(2, [11, 12])])), ('4', OrderedDict([(5, [14, 15])])),
                        ('7', OrderedDict([(8, [17, 18])]))]) == getattr(gcs, cmd)(['1', '4', '7'], [2, 5, 8])
    gcs.svr.queue(cmdstr(cmd, '1 2 4 5 7 8'), '1 2=11 12 \n4 5=14 15 \n7 8=17 18\n')
    assert OrderedDict([(1, OrderedDict([(2, [11, 12])])), ('4', OrderedDict([(5, [14, 15])])),
                        (7, OrderedDict([(8, [17, 18])]))]) == getattr(gcs, cmd)([1, '4', 7], [2, '5', '8'])
    checksvr(gcs)


def test_get_answer_with_spaces(gcs, cmd):
    """Controller sends answer with too many spaces."""
    PIDebug('enter test_get_2arg_[opt]_[opt]__{str_{int_[int_int]}}.test_get_answer_with_spaces(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), ' 1    2 = 11    12     \n    4  5\t=  14\t 15   \n    7    8  = 17    18\n')
    assert OrderedDict([('1', OrderedDict([(2, [11, 12])])), ('4', OrderedDict([(5, [14, 15])])),
                        ('7', OrderedDict([(8, [17, 18])]))]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_answer(gcs, cmd):
    """Controller sends wrong answer."""
    PIDebug('enter test_get_2arg_[opt]_[opt]__{str_{int_[int_int]}}.test_wrong_answer(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '1 2=11 12 \n4 w=14 15 \n7 8=17 18\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd), '1 2=11 12 \n4 5=1e4 15 \n7 8=17 18\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd), '1 2=11 12 \n4 5=14 15 \n7 8=17 1a8\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
