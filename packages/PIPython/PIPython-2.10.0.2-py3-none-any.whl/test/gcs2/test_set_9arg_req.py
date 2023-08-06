#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test setter commands with this signature: CMD req req req req req req req req req"""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
# Too many statements (53/50) pylint: disable=R0915
__signature__ = 0x1d5428faba16f58b1e9406fe29b58bd8

from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_set_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_set_9arg_req.test_set_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3 -4 5 -6 7 -8 9'))
    getattr(gcs, cmd)('1', 2.0, 3, -4.0, 5.0, -6.0, '7', -8, 9.0)
    gcs.svr.queue(cmdstr(cmd, 'a 2 3 -4 5 -6 b -8 9'))
    getattr(gcs, cmd)('a', 2.0, 3, -4.0, 5.0, -6.0, 'b', -8, 9.0)
    gcs.svr.queue(cmdstr(cmd, '1 2 3 -4 5 -6 7 -8 0'))
    getattr(gcs, cmd)(True, 2.0, 3, -4.0, 5.0, -6.0, '7', -8, False)
    checksvr(gcs)


def test_wrong_argtype(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_set_9arg_req.test_wrong_argtype(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2.1, 3], [2, 3, 4], ['3', 'a', 5], ['5', 'a', 5], ['5', 'a', 5], ['5', 'a', 5],
                          ['5', 'a', 5], ['5', 'a', 5], ['5', 'a', 5])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 3, 4, 5, 6, 7, 8, ['5', 'a', 5])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({'1': 2.1}, 2, 3, 4, 5, 6, 7, 8, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 3, 4, 5, 6, 7, 8, '')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('', '', '', '', '', '', '', '', '')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None, None, None, 4, 5, 6, 7, 8, 9)
    checksvr(gcs)


def test_set_list_scalar_args(gcs, cmd):
    """Arguments as lists and scalars mixed."""
    PIDebug('enter test_set_9arg_req.test_set_list_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3 4 5 6 7 8 9'))
    getattr(gcs, cmd)(['1'], [2], '3', '4', '5', [6], 7, 8, 9)
    gcs.svr.queue(cmdstr(cmd, '1 2 3 4 5 6 7 8 9'))
    getattr(gcs, cmd)(['1'], 2, ['3'], '4', 5, 6, 7, 8, [9])
    checksvr(gcs)


def test_missing_args(gcs, cmd):
    """No arguments, not enough arguments, empty strings, lists and dicts."""
    PIDebug('enter test_set_9arg_req.test_missing_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 3, 4, 5, 6, 7, 8)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('', '', '', '', '', '', '', '', '')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 3, 4, 5, 6, 7, 8, None)
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
