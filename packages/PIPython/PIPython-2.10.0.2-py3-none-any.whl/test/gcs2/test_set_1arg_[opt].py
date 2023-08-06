#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test setter commands with this signature: CMD [opt]"""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0x33578726aeed59237d7e7c5c5f2f6420

from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr
from test.gcs2.test_set_0arg import test_noraise

CMDS = [
    'CLR',
    'DFH',
    'DPO',
    'FNL',
    'FPL',
    'FRF',
    'GOH',
    'HLT',
    'INI',
    'ITD',
    'MNL',
    'MPL',
    'REF',
    'RST',
    'RTO',
    'SAV',
    'TGC',
    'TGS',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_set_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_set_1arg_[opt].test_set_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1'))
    getattr(gcs, cmd)(1)
    gcs.svr.queue(cmdstr(cmd, '2.34'))
    getattr(gcs, cmd)(2.34)
    gcs.svr.queue(cmdstr(cmd, 'b'))
    getattr(gcs, cmd)('b')
    gcs.svr.queue(cmdstr(cmd))
    getattr(gcs, cmd)()
    checksvr(gcs)


def test_set_list_args(gcs, cmd):
    """Arguments as lists."""
    PIDebug('enter test_set_1arg_[opt].test_set_list_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1.23 2.34'))
    getattr(gcs, cmd)([1.23, 2.34])
    gcs.svr.queue(cmdstr(cmd, 'a'))
    getattr(gcs, cmd)(['a'])
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    if cmd in ('HLT',):
        return
    PIDebug('enter test_set_1arg_[opt].test_set_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [5])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, [5])
    checksvr(gcs)


def test_set_no_args(gcs, cmd):
    """No arguments."""
    PIDebug('enter test_set_1arg_[opt].test_set_no_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd))
    getattr(gcs, cmd)()
    checksvr(gcs)


def test_noraise_clone(gcs, cmd):
    """Optional skipping GCS error 10 for stop commands."""
    if cmd not in ('HLT',):
        return
    PIDebug('enter test_set_1arg_[opt].test_noraise_clone(%s)', cmd)
    test_noraise(gcs, cmd)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
