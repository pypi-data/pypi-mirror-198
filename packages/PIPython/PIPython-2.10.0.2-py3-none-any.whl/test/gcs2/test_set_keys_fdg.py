#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test FDG command.
Not tested: Optional parameters need to be scalar, i.e. not list, tuple, dict.
"""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
__signature__ = 0xca8988786cb31ce6dd209a45599d1ac4

from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'FDG',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_missing_args(gcs, cmd):
    """Some required arguments are missing"""
    PIDebug('enter test_set_keys_fdg.test_missing_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, None)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, '')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, {})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)()
    checksvr(gcs)


def test_different_list_sizes(gcs, cmd):
    """Arguments as lists with different sizes."""
    PIDebug('enter test_set_keys_fdg.test_different_list_sizes(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1, 2], [1], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [1, 2], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [1], [1, 2])
    checksvr(gcs)


def test_wrong_argtype(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_set_keys_fdg.test_wrong_argtype(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2}, [1], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], {1: 2}, [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [1], {1: 2})
    checksvr(gcs)


def test_set_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_set_keys_fdg.test_set_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3'))
    getattr(gcs, cmd)('1', 2.0, 3.0)
    gcs.svr.queue(cmdstr(cmd, 'a b 3'))
    getattr(gcs, cmd)('a', 'b', 3.0)
    gcs.svr.queue(cmdstr(cmd, '1 -2 1'))
    getattr(gcs, cmd)('1', '-2', True)
    checksvr(gcs)


def test_set_list_scalar_args(gcs, cmd):
    """Arguments as lists and scalars mixed."""
    PIDebug('enter test_set_keys_fdg.test_set_list_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3'))
    getattr(gcs, cmd)(['1'], [2], '3')
    gcs.svr.queue(cmdstr(cmd, '1 2 3'))
    getattr(gcs, cmd)(['1'], 2, ['3'])
    gcs.svr.queue(cmdstr(cmd, '1 2 3'))
    getattr(gcs, cmd)('1', [2], '3')
    checksvr(gcs)


def test_set_all_args(gcs, cmd):
    """All arguments, different types."""
    PIDebug('enter test_set_keys_fdg.test_set_all_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 abc ML 4.56 A 5 MIA 6 MAA 7 F 8 SP def V 10 MDC 11 SPO 12'))
    getattr(gcs, cmd)(1, 2, 'abc', 4.56, 5, 6, 7, 8, 'def', 10, 11, 12)
    checksvr(gcs)


def test_set_keyword_args(gcs, cmd):
    """Some keyword arguments."""
    PIDebug('enter test_set_keys_fdg.test_set_keyword_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 abc ML 4.56 MIA 6 SP def V 10 SPO 12'))
    getattr(gcs, cmd)(1, 2, 'abc', minlevel=4.56, minampl=6, speedfactor='def', maxvelocity=10, speedoffset=12)
    gcs.svr.queue(cmdstr(cmd, '0 0 abc A 4.56 MAA 6 F def MDC 1'))
    getattr(gcs, cmd)(0, 0, 'abc', aligninputchannel=4.56, maxampl=6, frequency='def', maxdirectionchanges=1)
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
