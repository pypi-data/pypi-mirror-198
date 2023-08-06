#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test setter commands with this signature: CMD req."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
__signature__ = 0x3ac161f32465454d1fca8d2e75548d08

from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'AVG',
    'BDR',
    'CSV',
    'DEL',
    'KEN',
    'KLF',
    'KRM',
    'KSF',
    'MAC_BEG',
    'MAC_DEL',
    'MAC_STOP',
    'MEX',
    'RTR',
    'SCH',
    'TGT',
    'VLS',
    'DLT',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_set_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_set_1arg_req.test_set_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1'))
    getattr(gcs, cmd)(1)
    gcs.svr.queue(cmdstr(cmd, '2.34'))
    getattr(gcs, cmd)(2.34)
    gcs.svr.queue(cmdstr(cmd, 'b'))
    getattr(gcs, cmd)('b')
    checksvr(gcs)


def test_set_list_args(gcs, cmd):
    """Arguments as lists."""
    PIDebug('enter test_set_1arg_req.test_set_list_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '2.34'))
    getattr(gcs, cmd)([2.34])
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_set_1arg_req.test_set_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2})
    checksvr(gcs)


def test_missing_args(gcs, cmd):
    """No arguments, not enough arguments, empty strings, lists and dicts."""
    PIDebug('enter test_set_1arg_req.test_missing_args(%s)', cmd)
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
