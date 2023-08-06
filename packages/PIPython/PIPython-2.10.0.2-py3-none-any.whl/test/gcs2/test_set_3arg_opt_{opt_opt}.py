#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test setter commands with this signature: CMD opt {opt:opt}"""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0x65f85baeb60e4cfbec841298d4d3739

from collections import OrderedDict
from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'DPA',
    'WPA',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_set_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_set_3arg_opt_{opt_opt}.test_set_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '100'))
    getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd, '1'))
    getattr(gcs, cmd)('1')
    gcs.svr.queue(cmdstr(cmd, '1 2 3'))
    getattr(gcs, cmd)('1', 2.0, 3.0)
    gcs.svr.queue(cmdstr(cmd, 'a b 3'))
    getattr(gcs, cmd)('a', 'b', 3.0)
    gcs.svr.queue(cmdstr(cmd, '1 -2 0'))
    getattr(gcs, cmd)('1', '-2', False)
    checksvr(gcs)


def test_wrong_argtype(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_set_3arg_opt_{opt_opt}.test_wrong_argtype(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2.1, 3], {2: 3})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2.1, 3], [2, 3, 4], ['3', 'a', 5])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({'1': 2.1}, {2: 3}, {'3': 'a'})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({'1': 2.1}, {2: 3})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2.1})
    checksvr(gcs)


def test_set_dict_scalar_args(gcs, cmd):
    """Arguments as dicts and scalars mixed."""
    PIDebug('enter test_set_3arg_opt_{opt_opt}.test_set_dict_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3'))
    getattr(gcs, cmd)('1', {2: '3'})
    gcs.svr.queue(cmdstr(cmd, '1 2 3 4 5'))
    getattr(gcs, cmd)('1', OrderedDict([(2, '3'), (4, 5)]))
    gcs.svr.queue(cmdstr(cmd, '1'))
    getattr(gcs, cmd)('1', {})
    checksvr(gcs)


def test_set_list_scalar_args(gcs, cmd):
    """Arguments as lists and scalars mixed."""
    PIDebug('enter test_set_3arg_opt_{opt_opt}.test_set_list_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3'))
    getattr(gcs, cmd)(['1'], [2], '3')
    gcs.svr.queue(cmdstr(cmd, '1 2 3'))
    getattr(gcs, cmd)(['1'], 2, ['3'])
    gcs.svr.queue(cmdstr(cmd, '1 2 3'))
    getattr(gcs, cmd)('1', [2], '3')
    gcs.svr.queue(cmdstr(cmd, 'a 2 4 3 5'))
    getattr(gcs, cmd)('a', [2, 3], [4, 5])
    gcs.svr.queue(cmdstr(cmd, 'a'))
    getattr(gcs, cmd)('a', [], [])
    gcs.svr.queue(cmdstr(cmd, '3 1 2'))
    getattr(gcs, cmd)([3], 1, 2)
    gcs.svr.queue(cmdstr(cmd, '3'))
    getattr(gcs, cmd)([3])
    gcs.svr.queue(cmdstr(cmd, '100'))  # default for first param is "100"
    getattr(gcs, cmd)()
    checksvr(gcs)


def test_different_list_sizes(gcs, cmd):
    """Arguments as lists with different sizes."""
    PIDebug('enter test_set_3arg_opt_{opt_opt}.test_different_list_sizes(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('1', 2, [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({}, 2)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2], [1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1], [1, 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1], [2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1], [2, 3])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1, 2], [None])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1, 2], [None, 1])
    checksvr(gcs)


def test_missing_args(gcs, cmd):
    """No arguments, not enough arguments, empty strings, lists and dicts."""
    PIDebug('enter test_set_3arg_opt_{opt_opt}.test_missing_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([], [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({})
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
