#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test setter commands with this signature: CMD [req] [req] [req]"""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0xe605f3eb2ae0c950a798e40473dde2ab

from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'CTI',
    'CTO',
    'DRC',
    'FGC',
    'HDT',
    'HIL',
    'HIT',
    'JDT',
    'MOD',
    'SPA',
    'TWE',
    'TWS',
    'WTR',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_set_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_set_3arg_[req]_[req]_[req].test_set_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3'))
    getattr(gcs, cmd)('1', 2.0, 3.0)
    gcs.svr.queue(cmdstr(cmd, 'a 37 3'))
    getattr(gcs, cmd)('a', '37', 3.0)
    gcs.svr.queue(cmdstr(cmd, '1 -2 1'))
    getattr(gcs, cmd)('1', '-2', True)
    checksvr(gcs)


def test_set_list_args(gcs, cmd):
    """Arguments as lists."""
    PIDebug('enter test_set_3arg_[req]_[req]_[req].test_set_list_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3 2.1 3 a 3 4 5'))
    getattr(gcs, cmd)(['1', 2.1, 3], [2, 3, 4], ['3', 'a', 5])
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_set_3arg_[req]_[req]_[req].test_set_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2], [1], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1'], [1, '2'], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1'], [1], [1, True])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2}, [1], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1'], {1: 2}, [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1'], [1], {1: 2})
    checksvr(gcs)


def test_set_list_scalar_args(gcs, cmd):
    """Arguments as lists and scalars mixed."""
    PIDebug('enter test_set_3arg_[req]_[req]_[req].test_set_list_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3'))
    getattr(gcs, cmd)(['1'], [2], '3')
    gcs.svr.queue(cmdstr(cmd, '1 2 3'))
    getattr(gcs, cmd)(['1'], 2, ['3'])
    gcs.svr.queue(cmdstr(cmd, '1 2 3'))
    getattr(gcs, cmd)('1', [2], '3')
    checksvr(gcs)


def test_different_list_sizes(gcs, cmd):
    """Arguments as lists with different sizes."""
    PIDebug('enter test_set_3arg_[req]_[req]_[req].test_different_list_sizes(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1], [None, None])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2], [3, 4])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1], [2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1], [2, 3])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1, 2], [None])
    checksvr(gcs)


def test_missing_args(gcs, cmd):
    """No arguments, not enough arguments, empty strings, lists and dicts."""
    PIDebug('enter test_set_3arg_[req]_[req]_[req].test_missing_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([], [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([], [], [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({}, [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([], {})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None, [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)()
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({0: None})
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
