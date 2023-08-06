#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test command IsControllerReady."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
__signature__ = 0x20dafb32a9aa05e82ca823b6d3f08323

from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr

# Redefining built-in 'unichr' pylint: disable=W0622
# Invalid constant name "unichr" pylint: disable=C0103
try:
    unichr
except NameError:
    unichr = chr

CMDS = [
    'IsControllerReady',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_no_arg(gcs, cmd):
    """No arguments."""
    PIDebug('enter test_iscontrollerready.test_no_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '%s\n' % unichr(177))
    assert getattr(gcs, cmd)() is True
    gcs.svr.queue(cmdstr(cmd), '%s\n' % unichr(176))
    assert getattr(gcs, cmd)() is False
    checksvr(gcs)


def test_wrong_answer(gcs, cmd):
    """Controller sends wrong answer."""
    PIDebug('enter test_get_0arg__bool.test_wrong_answer(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '%s\n' % unichr(178))
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd), '%s\n' % unichr(175))
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd), '\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_0arg__bool.test_set_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1)
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
