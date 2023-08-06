#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test FIO command.
Not tested: Optional parameters need to be scalar, i.e. not list, tuple, dict.
"""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
__signature__ = 0xcff17ba9fa216ed5cbc142878af1056f

from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'FIO',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_missing_args(gcs, cmd):
    """Some required arguments are missing"""
    PIDebug('enter test_set_keys_fio.test_set_missing_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, None, 4)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, '', 4)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, [], 4)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, {}, 4)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 4)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)()
    checksvr(gcs)


def test_different_list_sizes(gcs, cmd):
    """Arguments as lists with different sizes."""
    PIDebug('enter test_set_keys_fio.test_set_different_list_sizes(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1, 2], [1], [1], [4])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [1, 2], [1], [4])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [1], [1, 2], [4])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [1], [2], [1, 4])
    checksvr(gcs)


def test_wrong_argtype(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_set_keys_fio.test_wrong_argtype(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2}, [1], [1], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], {1: 2}, [1], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [1], {1: 2}, [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [1], [1], {1: 2})
    checksvr(gcs)


def test_set_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_set_keys_fio.test_set_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3 4'))
    getattr(gcs, cmd)('1', 2.0, 3.0, '4')
    gcs.svr.queue(cmdstr(cmd, 'a b 3 4'))
    getattr(gcs, cmd)('a', 'b', 3.0, 4.0)
    gcs.svr.queue(cmdstr(cmd, '1 -2 1 4'))
    getattr(gcs, cmd)('1', '-2', True, 4)
    checksvr(gcs)


def test_set_list_scalar_args(gcs, cmd):
    """Arguments as lists and scalars mixed."""
    PIDebug('enter test_set_keys_fio.test_set_list_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3 4'))
    getattr(gcs, cmd)(['1'], [2], '3', [4])
    gcs.svr.queue(cmdstr(cmd, '1 2 3 4'))
    getattr(gcs, cmd)(['1'], 2, ['3'], 4)
    gcs.svr.queue(cmdstr(cmd, '1 2 3 4'))
    getattr(gcs, cmd)('1', [2], '3', '4')
    checksvr(gcs)


def test_set_all_args(gcs, cmd):
    """All arguments, different types."""
    PIDebug('enter test_set_keys_fio.test_set_all_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, 'Y 0.1 Z 0.1 S 0.01 AR 0.1 L 1 A 2'))
    getattr(gcs, cmd)('Y', 0.1, 'Z', 0.1, 0.01, 0.1, 1.0, 2)
    checksvr(gcs)


def test_set_keyword_args(gcs, cmd):
    """Some keyword arguments."""
    PIDebug('enter test_set_keys_fio.test_set_keyword_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, 'A 2 B 4.56 S 1'))
    getattr(gcs, cmd)('A', 2.0, 'B', 4.56, 1.0)
    gcs.svr.queue(cmdstr(cmd, 'A 2 B 4.56 S 1 AR 2'))
    getattr(gcs, cmd)('A', 2.0, 'B', 4.56, 1.0, 2.0)
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
