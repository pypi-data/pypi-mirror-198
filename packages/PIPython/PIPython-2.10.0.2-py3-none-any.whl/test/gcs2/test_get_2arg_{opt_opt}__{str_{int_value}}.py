#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning a dict of str/int/value with this signature: CMD {opt:opt}."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0x40babc23d98e5cdf6189fd6c20d11f95

from pipython import PIDebug

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'qSEP',
    'qSPA',
]


@pytest.fixture(scope='module', autouse=True)
def set_qhpa_answer(gcs):
    """Setup and teardown qHPA answer for parameter value conversion."""
    gcs.svr.append('HPA?\n', '0x2=\t0\t4\tFLOAT\tmotorcontroller\tP term \n'
                             '0x7=\t0\t4\tCHAR\tmotorcontroller\tP term \n'
                             '0xb=\t0\t4\tINT\tmotorcontroller\tP term\n')
    yield  # teardown is below
    gcs.clearparamconv()
    gcs.svr.clear()


@pytest.fixture(scope='module', params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_get_noargs(gcs, cmd):
    """No arguments. Will return converted "items"."""
    PIDebug('enter test_get_2arg_{opt_opt}__{str_{int_value}}.test_get_noargs(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '1 2=1.23 \n2 0xb=1 \n3 7=foo\n')
    assert OrderedDict([('1', OrderedDict([(2, 1.23)])), ('2', OrderedDict([(11, 1)])),
                        ('3', OrderedDict([(7, 'foo')]))]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_2arg_{opt_opt}__{str_{int_value}}.test_wrong_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, ['1', 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, {1: 2})
    checksvr(gcs)


def test_no_int_conv(gcs, cmd):
    """No integer conversion of integer like strings."""
    PIDebug('enter test_get_2arg_{opt_opt}__{str_{int_value}}.test_no_int_conv(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '3 7'), '3 7=0000123456\n')
    gcs.svr.queue(cmdstr(cmd, '3 7'), '3 7=0000123456\n')
    assert OrderedDict([('3', OrderedDict([(7, '0000123456')]))]) == getattr(gcs, cmd)('3', '7')
    assert OrderedDict([(3, OrderedDict([(7, '0000123456')]))]) == getattr(gcs, cmd)(3, 7)
    checksvr(gcs)


def test_get_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_get_2arg_{opt_opt}__{str_{int_value}}.test_get_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2'), '1 2=1.23\n')
    gcs.svr.queue(cmdstr(cmd, '1 2'), '1 2=1.23\n')
    assert OrderedDict([('1', OrderedDict([(2, 1.23)]))]) == getattr(gcs, cmd)('1', '2')
    assert OrderedDict([(1, OrderedDict([(2, 1.23)]))]) == getattr(gcs, cmd)(1, 2)
    gcs.svr.queue(cmdstr(cmd, '2 11'), '2 0xb=1\n')
    gcs.svr.queue(cmdstr(cmd, '2 11'), '2 0xb=1\n')
    assert OrderedDict([('2', OrderedDict([(11, 1)]))]) == getattr(gcs, cmd)('2', 'b')
    assert OrderedDict([(2, OrderedDict([(11, 1)]))]) == getattr(gcs, cmd)(2, 11)
    gcs.svr.queue(cmdstr(cmd, '3 7'), '3 7=foo\n')
    gcs.svr.queue(cmdstr(cmd, '3 7'), '3 7=foo\n')
    assert OrderedDict([('3', OrderedDict([(7, 'foo')]))]) == getattr(gcs, cmd)('3', '7')
    assert OrderedDict([(3, OrderedDict([(7, 'foo')]))]) == getattr(gcs, cmd)(3, 7)
    checksvr(gcs)


def test_get_list_args(gcs, cmd):
    """Arguments as lists."""
    PIDebug('enter test_get_2arg_{opt_opt}__{str_{int_value}}.test_get_list_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 2 11'), '1 2=1.23 \n2 0xb=1\n')
    gcs.svr.queue(cmdstr(cmd, '1 2 2 11'), '1 2=1.23 \n2 0xb=1\n')
    assert OrderedDict([('1', OrderedDict([(2, 1.23)])),
                        ('2', OrderedDict([(11, 1)]))]) == getattr(gcs, cmd)(['1', '2'], ['2', 'b'])
    assert OrderedDict([(1, OrderedDict([(2, 1.23)])),
                        (2, OrderedDict([(11, 1)]))]) == getattr(gcs, cmd)([1, 2], [2, 11])
    checksvr(gcs)


def test_get_answer_with_spaces(gcs, cmd):
    """Controller sends answer with too many spaces."""
    PIDebug('enter test_get_2arg_{opt_opt}__{str_{int_value}}.test_get_answer_with_spaces(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), ' 1   2 =   1.23   \n  2   0xb = 1  \n  3  7 =foo\n')
    assert OrderedDict([('1', OrderedDict([(2, 1.23)])), ('2', OrderedDict([(11, 1)])),
                        ('3', OrderedDict([(7, 'foo')]))]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_answer(gcs, cmd):
    """Controller sends wrong answer."""
    PIDebug('enter test_get_2arg_{opt_opt}__{str_{int_value}}.test_wrong_answer(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '1 a=1.23 \n2 0xb=1 \n3 7=foo\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    checksvr(gcs)



import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
