#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning a string with this signature: CMD opt opt."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
__signature__ = 0x4316645261b82947f9d624d000992c4

from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'qKLT',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_get_no_args(gcs, cmd):
    """No arguments."""
    PIDebug('enter test_get_2arg_opt_opt__str.test_get_no_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), 'foo \nbar\n')
    assert 'foo \nbar\n' == getattr(gcs, cmd)()
    checksvr(gcs)


def test_get_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_get_2arg_opt_opt__str.test_get_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1'), 'foo \nbar\n')
    assert 'foo \nbar\n' == getattr(gcs, cmd)('1')
    gcs.svr.queue(cmdstr(cmd, '1 2'), 'foo \nbar\n')
    assert 'foo \nbar\n' == getattr(gcs, cmd)(1, 2)
    checksvr(gcs)


def test_get_list_args(gcs, cmd):
    """Arguments as lists."""
    PIDebug('enter test_get_2arg_opt_opt__str.test_get_list_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1'), 'foo \nbar\n')
    assert 'foo \nbar\n' == getattr(gcs, cmd)(['1'])
    gcs.svr.queue(cmdstr(cmd, '1 2'), 'foo \nbar\n')
    assert 'foo \nbar\n' == getattr(gcs, cmd)([1], ['2'])
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_2arg_opt_opt__str.test_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, ['1', 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 3)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, {1: 2})
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
