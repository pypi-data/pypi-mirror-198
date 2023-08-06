#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning a float with this signature: CMD req req."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
__signature__ = 0xc57bbcc5b18674f15e547719ad0683e2

from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'qSWT',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_get_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_get_2arg_req_req__float.test_get_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2'), '17.3\n')
    assert 17.3 == getattr(gcs, cmd)('1', 2)
    gcs.svr.queue(cmdstr(cmd, '1 2'), '17.3\n')
    assert 17.3 == getattr(gcs, cmd)(1, '2')
    checksvr(gcs)


def test_get_list_args(gcs, cmd):
    """Arguments as lists."""
    PIDebug('enter test_get_2arg_req_req__float.test_get_list_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2'), '17.3\n')
    assert 17.3 == getattr(gcs, cmd)(['1'], [2])
    gcs.svr.queue(cmdstr(cmd, '1 2'), '17.3\n')
    assert 17.3 == getattr(gcs, cmd)([1], ['2'])
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_2arg_req_req__float.test_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2], 1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, ['1', 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 3)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2}, 1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, {1: 2})
    checksvr(gcs)


def test_missing_args(gcs, cmd):
    """No arguments, not enough arguments, empty strings, lists and dicts."""
    PIDebug('enter test_get_2arg_req_req__float.test_missing_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)()
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, None)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, '')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, {})
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
