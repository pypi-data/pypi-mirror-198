#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test MAT command."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
# Too many statements (53/50) pylint: disable=R0915
__signature__ = 0xecb2745e331412acdd0c42e54a9db305

from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'MAT',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_set_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_mat.test_set_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 = 2 * -4.1'))
    getattr(gcs, cmd)('1', 2.0, '*', -4.1)
    gcs.svr.queue(cmdstr(cmd, 'a = b OR 0'))
    getattr(gcs, cmd)('a', 'b', 'OR', False)
    gcs.svr.queue(cmdstr(cmd, '1 = -2.20 1 2'))
    getattr(gcs, cmd)('1', '-2.20', True, 2)
    checksvr(gcs)


def test_wrong_argtype(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_mat.test_wrong_argtype(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2.1, 3], [2, 3, 4], ['3', 'a', 5], ['5', 'a', 5], ['5', 'a', 5])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2.1, 3], [2, 3, 4], ['3', 'a', 5], ['5', 'a', 5])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({'1': 2.1}, {2: 3}, {'3': 'a'}, {'3': 'a'})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({'1': 2.1}, {2: 3}, {'3': 'a'})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2.1}, 1, 1, 4)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2.1}, 1, 1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2.1, 3], [2, 3, 4], ['3', 'a', 5])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({'1': 2.1}, {2: 3}, {'3': 'a'}, {'3': 'a'})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({'1': 2.1}, {2: 3}, {'3': 'a'})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2.1}, 1, 1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, {1: 2.1}, 4)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, {1: 2.1}, 1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 1, {1: 2.1}, 4)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 1, {1: 2.1})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 1, '', 2)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('', '', '', '')
    checksvr(gcs)


def test_set_list_scalar_args(gcs, cmd):
    """Arguments as lists and scalars mixed."""
    PIDebug('enter test_mat.test_set_list_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 = 2 3 4'))
    getattr(gcs, cmd)(['1'], [2], '3', '4')
    gcs.svr.queue(cmdstr(cmd, '1 = 2 3 4'))
    getattr(gcs, cmd)(['1'], 2, ['3'], '4')
    gcs.svr.queue(cmdstr(cmd, '1 = 2 3 4'))
    getattr(gcs, cmd)('1', [2], '3', 4)
    gcs.svr.queue(cmdstr(cmd, '1 = 2 3 4'))
    getattr(gcs, cmd)([1], [2], [3], [4])
    checksvr(gcs)


def test_different_list_sizes(gcs, cmd):
    """Arguments as lists with different sizes."""
    PIDebug('enter test_mat.test_different_list_sizes(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1], [None, None])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1], [None, None], True)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2], [1], False)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2], [3, 4], '3')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2], [3, 4])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2], [3, 4], [4])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1], [2], [None])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1], [2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1], [2, 3], '2')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1], [2, 3])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1, 2], [None])
    checksvr(gcs)


def test_missing_args(gcs, cmd):
    """No arguments, not enough arguments, empty strings, lists and dicts."""
    PIDebug('enter test_mat.test_missing_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('1', [], [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('1', [], [], [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('1', 2, [], '3')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('1', 2, [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({}, 2)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({}, 2, 3)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 5)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([], [], [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([], [], [], [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([], [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([], [], [4])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None, [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 4)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1, 2, 3, 4])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [2], [3], '')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None, None, None, '')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)()
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({}, {}, {}, {})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({0: None})
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
