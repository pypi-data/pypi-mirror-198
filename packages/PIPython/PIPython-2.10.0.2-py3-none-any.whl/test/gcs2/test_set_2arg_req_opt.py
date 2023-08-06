#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test setter commands with this signature: CMD req opt"""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
__signature__ = 0x740a85ea9953c597a435c4e24953106c

from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'CCL',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_set_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_set_2arg_req_opt.test_set_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2.34'))
    getattr(gcs, cmd)('1', 2.34)
    gcs.svr.queue(cmdstr(cmd, '1 2.34'))
    getattr(gcs, cmd)(1, '2.34')
    gcs.svr.queue(cmdstr(cmd, 'b a'))
    getattr(gcs, cmd)('b', 'a')
    gcs.svr.queue(cmdstr(cmd, '1 a'))
    getattr(gcs, cmd)(['1'], ['a'])
    checksvr(gcs)


def test_set_one_arg(gcs, cmd):
    """One argument."""
    PIDebug('enter test_set_2arg_req_opt.test_set_one_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1'))
    getattr(gcs, cmd)('1')
    gcs.svr.queue(cmdstr(cmd, '1'))
    getattr(gcs, cmd)(True)
    gcs.svr.queue(cmdstr(cmd, 17))
    getattr(gcs, cmd)(17)
    gcs.svr.queue(cmdstr(cmd, 'ba'))
    getattr(gcs, cmd)('ba')
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_set_2arg_req_opt.test_set_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2], [2.34, 4.56])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([], [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({'1': 2.34})
    checksvr(gcs)


def test_set_list_args(gcs, cmd):
    """Arguments as lists."""
    PIDebug('enter test_set_2arg_{req_opt}.py.test_set_list_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 a'))
    getattr(gcs, cmd)([1], ['a'])
    checksvr(gcs)


def test_set_list_scalar_args(gcs, cmd):
    """Arguments as lists and scalars."""
    PIDebug('enter test_set_2arg_req_opt.test_set_list_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2.34'))
    getattr(gcs, cmd)(['1'], 2.34)
    gcs.svr.queue(cmdstr(cmd, '1 2.34'))
    getattr(gcs, cmd)([1], '2.34')
    gcs.svr.queue(cmdstr(cmd, '1 2.34'))
    getattr(gcs, cmd)('1', [2.34])
    gcs.svr.queue(cmdstr(cmd, '1 2.34'))
    getattr(gcs, cmd)(1, ['2.34'])
    gcs.svr.queue(cmdstr(cmd, '1'))
    getattr(gcs, cmd)(1)
    checksvr(gcs)


def test_different_list_sizes(gcs, cmd):
    """Arguments as lists with different sizes."""
    PIDebug('enter test_set_2arg_{req_opt}.py.test_different_list_sizes(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1])
    checksvr(gcs)


def test_missing_args(gcs, cmd):
    """No arguments, not enough arguments, empty strings, lists and dicts."""
    PIDebug('enter test_set_2arg_req_opt.test_missing_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)()
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({})
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
