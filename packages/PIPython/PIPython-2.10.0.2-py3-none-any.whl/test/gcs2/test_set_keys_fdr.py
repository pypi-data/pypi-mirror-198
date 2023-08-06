#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test FDR command.
Not tested: Optional parameters need to be scalar, i.e. not list, tuple, dict.
"""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
__signature__ = 0x846f171059b4dc4b0e4383eb66b33da

from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'FDR',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_missing_args(gcs, cmd):
    """Some required arguments are missing"""
    PIDebug('enter test_set_keys_fdr.test_missing_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 3, 4, None)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 3, 4, '')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 3, 4, [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 3, 4, {})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 3, 4)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)()
    checksvr(gcs)


def test_different_list_sizes(gcs, cmd):
    """Arguments as lists with different sizes."""
    PIDebug('enter test_set_keys_fdr.test_different_list_sizes(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1, 2], [1], [1], [1], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [1, 2], [1], [1], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [1], [1, 2], [1], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [1], [1], [1, 2], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [1], [1], [1], [1, 2])
    checksvr(gcs)


def test_wrong_argtype(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_set_keys_fdr.test_wrong_argtype(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2}, [1], [1], [1], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], {1: 2}, [1], [1], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [1], {1: 2}, [1], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [1], [1], {1: 2}, [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [1], [1], [1], {1: 2})
    checksvr(gcs)


def test_set_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_set_keys_fdr.test_set_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3 4 1'))
    getattr(gcs, cmd)('1', 2.0, 3.0, 4, True)
    gcs.svr.queue(cmdstr(cmd, 'a b 3 4 5'))
    getattr(gcs, cmd)('a', 'b', 3.0, '4', '5')
    gcs.svr.queue(cmdstr(cmd, '1 -2 1 0 0'))
    getattr(gcs, cmd)('1', '-2', True, False, False)
    checksvr(gcs)


def test_set_list_scalar_args(gcs, cmd):
    """Arguments as lists and scalars mixed."""
    PIDebug('enter test_set_keys_fdr.test_set_list_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3 4 5'))
    getattr(gcs, cmd)(['1'], [2], '3', 4, 5)
    gcs.svr.queue(cmdstr(cmd, '1 2 3 4 5'))
    getattr(gcs, cmd)(['1'], 2, ['3'], 4, 5)
    gcs.svr.queue(cmdstr(cmd, '1 2 3 4 5'))
    getattr(gcs, cmd)('1', [2], '3', 4, [5])
    checksvr(gcs)


def test_set_all_args(gcs, cmd):
    """All arguments, different types."""
    PIDebug('enter test_set_keys_fdr.test_set_all_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 abc 4.56 5 L 6 A 7 F 8 V def MP1 10 MP2 11 TT 12 CM 13 MIIL 14 MAIL 15 ST 16'))
    getattr(gcs, cmd)(1, 2, 'abc', 4.56, 5, 6, 7, 8, 'def', 10, 11, 12, 13, 14, 15, 16)
    checksvr(gcs)


def test_set_keyword_args(gcs, cmd):
    """Some keyword arguments."""
    PIDebug('enter test_set_keys_fdr.test_set_keyword_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 abc 4.56 5 L 6 F 7 V 8 TT 9 CM 0'))
    getattr(gcs, cmd)(1, 2, 'abc', 4.56, 5, threshold='6', frequency=7, velocity=8, targettype=9, estimationmethod=0)
    gcs.svr.queue(cmdstr(cmd, '1 2 abc 4.56 5 A 6 MP1 7 MP2 8 ST 9'))
    getattr(gcs, cmd)(1, 2, 'abc', 4.56, 5, aligninputchannel='6', scanmiddlepos=7, stepmiddlepos=8, stopoption=9)
    gcs.svr.queue(cmdstr(cmd, '1 2 abc 4.56 5 MIIL 6 MAIL 7'))
    getattr(gcs, cmd)(1, 2, 'abc', 4.56, 5, mininput='6', maxinput=7)
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
