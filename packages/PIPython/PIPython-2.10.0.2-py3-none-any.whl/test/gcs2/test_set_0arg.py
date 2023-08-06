#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test setter commands with this signature: CMD."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
__signature__ = 0x86504a49e7dce6c54e6d349c09a06533

from pipython import PIDebug

import pytest

from pipython import GCSError
from test.tools import checksvr, cmdstr

CMDS = [
    'MAC_END',
    'RBT',
    'StopAll',
    'STF',
    'STP',
    'TWC',
    'WGR',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_set_no_args(gcs, cmd):
    """No arguments."""
    PIDebug('enter test_set_0arg.test_set_no_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd))
    getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    if cmd in ('StopAll', 'STP', 'STF'):
        return
    PIDebug('enter test_set_0arg.test_set_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1)
    checksvr(gcs)


def test_noraise(gcs, cmd):
    """Optional skipping GCS error 10 for stop commands."""
    if cmd not in ('StopAll', 'STP', 'HLT',):
        return
    PIDebug('enter test_set_0arg.test_noraise(%s)', cmd)
    gcs.errcheck = True
    gcs.svr.queue(cmdstr(cmd))
    gcs.svr.queue('ERR?\n', '10\n')
    with pytest.raises(GCSError):
        getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd))
    gcs.svr.queue('ERR?\n', '17\n')
    with pytest.raises(GCSError):
        getattr(gcs, cmd)(noraise=True)
    gcs.svr.queue(cmdstr(cmd))
    gcs.svr.queue('ERR?\n', '10\n')
    getattr(gcs, cmd)(noraise=True)
    gcs.errcheck = False
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
