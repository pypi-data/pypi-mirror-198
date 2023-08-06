#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning a float with this signature: CMD."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
__signature__ = 0x53d99008c51ab31188505f8f2ad03e80

from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'qCSV',
    'qTIM',
    'qVLS',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_no_arg(gcs, cmd):
    """No arguments."""
    PIDebug('enter test_get_0arg__float.test_no_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '-18.3\n')
    assert -18.3 == getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd), '32301\n')
    assert 32301 == getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_answer(gcs, cmd):
    """Controller sends wrong answer."""
    PIDebug('enter test_get_0arg__float.test_wrong_answer(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), 'a\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd), '/1\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_0arg__float.test_set_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1)
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
