#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test setter commands with this signature: CMD [req]."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0x4c4b346e0865f7eac6dbd0ae138ca744

from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'DTC',
    'FPH',
    'FRS',
    'TGF',
    'WCL',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_set_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_set_1arg_[req].test_set_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1'))
    getattr(gcs, cmd)(1)
    gcs.svr.queue(cmdstr(cmd, '2.34'))
    getattr(gcs, cmd)(2.34)
    gcs.svr.queue(cmdstr(cmd, 'b'))
    getattr(gcs, cmd)('b')
    checksvr(gcs)


def test_set_list_args(gcs, cmd):
    """Arguments as lists."""
    PIDebug('enter test_set_1arg_[req].test_set_list_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1.23 2.34'))
    getattr(gcs, cmd)([1.23, 2.34])
    gcs.svr.queue(cmdstr(cmd, 'a'))
    getattr(gcs, cmd)(['a'])
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_set_1arg_[req].test_set_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [5])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, [5])
    checksvr(gcs)


def test_missing_args(gcs, cmd):
    """No arguments, not enough arguments, empty strings, lists and dicts."""
    PIDebug('enter test_set_1arg_[req].test_missing_args(%s)', cmd)
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
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
