#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test "VER?" command with this signature: CMD."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
__signature__ = 0x9c23330a72c482e97633e2c042e039d

from pipython import PIDebug

import pytest

from pipython import __version__
from test.tools import checksvr, cmdstr

CMDS = [
    'qVER',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_no_arg(gcs, cmd):
    """No arguments."""
    PIDebug('enter test_get_0arg__str_qver.test_no_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), 'foo bar\n')
    assert 'foo bar \nPIPython: %s\n' % __version__ == getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd), 'foo \nbar\n')
    assert 'foo \nbar \nPIPython: %s\n' % __version__ == getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_0arg__str_qver.test_set_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1)
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
