#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test FSA command.
Not tested: Optional parameters need to be scalar, i.e. not list, tuple, dict.
"""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
__signature__ = 0xf798d24e315021ce5f18afe433d02265

from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'FSA',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_missing_args(gcs, cmd):
    """Some required arguments are missing"""
    PIDebug('enter test_set_keys_fsa.test_set_missing_args(%s)', cmd)
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
    PIDebug('enter test_set_keys_fsa.test_set_different_list_sizes(%s)', cmd)
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
    PIDebug('enter test_set_keys_fsa.test_wrong_argtype(%s)', cmd)
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
    PIDebug('enter test_set_keys_fsa.test_set_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3 4'))
    getattr(gcs, cmd)('1', 2.0, 3.0, '4')
    gcs.svr.queue(cmdstr(cmd, 'a b 3 4'))
    getattr(gcs, cmd)('a', 'b', 3.0, 4.0)
    gcs.svr.queue(cmdstr(cmd, '1 -2 1 4'))
    getattr(gcs, cmd)('1', '-2', True, 4)
    checksvr(gcs)


def test_set_list_scalar_args(gcs, cmd):
    """Arguments as lists and scalars mixed."""
    PIDebug('enter test_set_keys_fsa.test_set_list_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3 4'))
    getattr(gcs, cmd)(['1'], [2], '3', [4])
    gcs.svr.queue(cmdstr(cmd, '1 2 3 4'))
    getattr(gcs, cmd)(['1'], 2, ['3'], 4)
    gcs.svr.queue(cmdstr(cmd, '1 2 3 4'))
    getattr(gcs, cmd)('1', [2], '3', '4')
    checksvr(gcs)


def test_set_all_args(gcs, cmd):
    """All arguments, different types."""
    PIDebug('enter test_set_keys_fsa.test_set_all_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, 'Q 0.1 P 0.2 L 1 S 0.01 SA 1 A 2'))
    getattr(gcs, cmd)('Q', 0.1, 'P', 0.2, 1.0, 0.01, 0o01, 2)
    checksvr(gcs)


def test_set_keyword_args(gcs, cmd):
    """Some keyword arguments."""
    PIDebug('enter test_set_keys_fsa.test_set_keyword_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, 'Q 0.1 P 0.2 L 1'))
    getattr(gcs, cmd)('Q', 0.1, 'P', 0.2, 1.0)
    gcs.svr.queue(cmdstr(cmd, 'Q 0.1 P 0.2 L 1 S 0.01'))
    getattr(gcs, cmd)('Q', 0.1, 'P', 0.2, 1.0, 0.01)
    gcs.svr.queue(cmdstr(cmd, 'Q 0.1 P 0.2 L 1 S 0.01 SA 1'))
    getattr(gcs, cmd)('Q', 0.1, 'P', 0.2, 1.0, 0.01, 0o01)
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
