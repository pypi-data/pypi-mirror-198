#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test FLM_FLS command.
Not tested: Optional parameters need to be scalar, i.e. not list, tuple, dict.
"""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
__signature__ = 0xcc89d8183cbfd91aa7091553c4d792a

from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'FLM',
    'FLS',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_missing_args(gcs, cmd):
    """Some required arguments are missing"""
    PIDebug('enter test_set_keys_flm_fls.test_set_missing_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, None)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, '')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([], 2)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, {})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)()
    checksvr(gcs)


def test_different_list_sizes(gcs, cmd):
    """Arguments as lists with different sizes."""
    PIDebug('enter test_set_keys_flm_fls.test_set_different_list_sizes(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1, 2], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [1, 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [])
    checksvr(gcs)


def test_wrong_argtype(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_set_keys_flm_fls.test_wrong_argtype(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2}, [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], {1: 2})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1, 2], 1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1, 3, 2], '1')
    checksvr(gcs)


def test_set_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_set_keys_flm_fls.test_set_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2'))
    getattr(gcs, cmd)('1', 2.0)
    gcs.svr.queue(cmdstr(cmd, 'a b'))
    getattr(gcs, cmd)('a', 'b')
    gcs.svr.queue(cmdstr(cmd, '1 -2'))
    getattr(gcs, cmd)(True, '-2')
    checksvr(gcs)


def test_set_list_scalar_args(gcs, cmd):
    """Arguments as lists and scalars mixed."""
    PIDebug('enter test_set_keys_flm_fls.test_set_list_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2'))
    getattr(gcs, cmd)(['1'], [2])
    gcs.svr.queue(cmdstr(cmd, '1 2'))
    getattr(gcs, cmd)(['1'], 2)
    gcs.svr.queue(cmdstr(cmd, '1 2'))
    getattr(gcs, cmd)('1', [2])
    checksvr(gcs)


def test_set_all_args(gcs, cmd):
    """All arguments, different types."""
    PIDebug('enter test_set_keys_flm_fls.test_set_all_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, 'Q 3 L 5 A 2 D 0'))
    getattr(gcs, cmd)('Q', 3, 5.0, 2, 0)
    checksvr(gcs)


def test_set_keyword_args(gcs, cmd):
    """Some keyword arguments."""
    PIDebug('enter test_set_keys_flm_fls.test_set_keyword_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, 'Q 3 L 5'))
    getattr(gcs, cmd)('Q', 3, 5.0)
    gcs.svr.queue(cmdstr(cmd, 'Q 3 L 5 A 2'))
    getattr(gcs, cmd)('Q', 3, 5.0, 2)
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
