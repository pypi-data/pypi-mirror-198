#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test setter commands with this signature: CMD {opt_opt}."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0xa6ade5e90246282b6b1e11bfacaeef9a

from collections import OrderedDict
from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'ATZ',
    'RPA',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_set_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_set_2arg_{opt_opt}.py.test_set_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2.34'))
    getattr(gcs, cmd)('1', 2.34)
    gcs.svr.queue(cmdstr(cmd, '0 2.34'))
    getattr(gcs, cmd)(False, '2.34')
    gcs.svr.queue(cmdstr(cmd, 'b a'))
    getattr(gcs, cmd)('b', 'a')
    gcs.svr.queue(cmdstr(cmd, ''))
    getattr(gcs, cmd)('', '')
    gcs.svr.queue(cmdstr(cmd))
    getattr(gcs, cmd)()
    checksvr(gcs)


def test_set_dict_arg(gcs, cmd):
    """Arguments as dict."""
    PIDebug('enter test_set_2arg_{opt_opt}.py.test_set_dict_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2.34 2 abc 3 1'))
    getattr(gcs, cmd)(OrderedDict([('1', 2.34), (2, 'abc'), ('3', True)]))
    gcs.svr.queue(cmdstr(cmd, '1 -2.34'))
    getattr(gcs, cmd)({'1': -2.34})
    gcs.svr.queue(cmdstr(cmd, ''))
    getattr(gcs, cmd)({})
    checksvr(gcs)


def test_set_list_args(gcs, cmd):
    """Arguments as lists."""
    PIDebug('enter test_set_2arg_{opt_opt}.py.test_set_list_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2.34 2 4.56 3 6.78'))
    getattr(gcs, cmd)(['1', 2, '3'], [2.34, 4.56, '6.78'])
    gcs.svr.queue(cmdstr(cmd, '1 1'))
    getattr(gcs, cmd)(['1'], [True])
    gcs.svr.queue(cmdstr(cmd, ''))
    getattr(gcs, cmd)([], [])
    checksvr(gcs)


def test_set_list_scalar_args(gcs, cmd):
    """Arguments as lists and scalars mixed."""
    PIDebug('enter test_set_2arg_{opt_opt}.py.test_set_list_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2.34'))
    getattr(gcs, cmd)(['1'], 2.34)
    gcs.svr.queue(cmdstr(cmd, '1 2.34'))
    getattr(gcs, cmd)([1], '2.34')
    gcs.svr.queue(cmdstr(cmd, '1 2.34'))
    getattr(gcs, cmd)('1', [2.34])
    gcs.svr.queue(cmdstr(cmd, '1 -2.34'))
    getattr(gcs, cmd)(1, ['-2.34'])
    gcs.svr.queue(cmdstr(cmd, ''))
    getattr(gcs, cmd)('', [])
    checksvr(gcs)


def test_different_list_sizes(gcs, cmd):
    """Arguments as lists with different sizes."""
    PIDebug('enter test_set_2arg_{opt_opt}.py.test_different_list_sizes(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1])
    checksvr(gcs)


def test_missing_args(gcs, cmd):
    """No arguments, not enough arguments, empty strings, lists and dicts."""
    PIDebug('enter test_set_2arg_{opt_opt}.py.test_missing_args(%s)', cmd)

    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1])

    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
