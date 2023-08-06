#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning a string with this signature: CMD."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
__signature__ = 0x15b8e8547469e56d64b7fa4e73499cff

from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'qFRH',
    'qHDI',
    'qHDR',
    'qHLP',
    'qHPA',
    'qHPV',
    'qIDN',
    'qRMC',
    'qSCH',
    'qSSN',
    'qTVI',
    'qLST',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_no_arg(gcs, cmd):
    """No arguments."""
    PIDebug('enter test_get_0arg__str.test_no_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), 'foo bar\n')
    assert 'foo bar\n' == getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd), 'foo \nbar\n')
    assert 'foo \nbar\n' == getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_0arg__str.test_set_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1)
    checksvr(gcs)


def test_long_answer(gcs, cmd):
    """One long line."""
    PIDebug('enter test_get_0arg__str.test_long_answer(%s)', cmd)
    msg = ' '.join(str(x) for x in range(10000))
    msg += '\n'
    gcs.svr.queue(cmdstr(cmd), msg)
    assert msg == getattr(gcs, cmd)()
    checksvr(gcs)


def test_many_lines(gcs, cmd):
    """Many lines."""
    PIDebug('enter test_get_0arg__str.test_many_lines(%s)', cmd)
    msg = ' \n'.join(str(x) for x in range(1000))
    msg += 'end\n'
    gcs.svr.queue(cmdstr(cmd), msg)
    assert msg == getattr(gcs, cmd)()
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
