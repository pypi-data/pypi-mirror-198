#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning an int with this signature: CMD."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
__signature__ = 0x288313fdb5c9352c91f998b74bb53e5f

from pipython import PIDebug

import pytest

from pipython import GCSError
from test.tools import checksvr, cmdstr

CMDS = [
    'GetDynamicMoveBufferSize',
    'MAC_qFREE',
    'qAVG',
    'qBDR',
    'qCCL',
    'qERR',
    'qFSS',
    'qRTR',
    'qSTA',
    'qTAC',
    'qTGT',
    'qTLT',
    'qTNJ',
    'qTNR',
    'qTPC',
    'qTSC',
    'qTWG',
    'qTWT',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_no_arg(gcs, cmd):
    """No arguments."""
    PIDebug('enter test_get_0arg__int.test_no_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '8\n')
    assert 8 == getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd), '323\n')
    assert getattr(gcs, cmd)() in (323, 803)  # dec, hex
    checksvr(gcs)


def test_wrong_answer(gcs, cmd):
    """Controller sends wrong answer."""
    PIDebug('enter test_get_0arg__int.test_wrong_answer(%s)', cmd)
    expectederror = GCSError if 'qERR' == cmd else ValueError
    gcs.svr.queue(cmdstr(cmd), 'g\n')
    with pytest.raises(expectederror):
        getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd), '/1\n')
    with pytest.raises(expectederror):
        getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_0arg__int.test_set_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1)
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
