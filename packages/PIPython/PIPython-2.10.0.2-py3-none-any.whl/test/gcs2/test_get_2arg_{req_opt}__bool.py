#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning a bool with this signature: CMD {req_opt}."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0x4350eaa230cb8273df6fcb1ba2eb2164

from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'qVMO',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_get_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_get_2arg_{req_opt}__bool.test_get_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2'), '1\n')
    assert getattr(gcs, cmd)('1', 2) is True
    gcs.svr.queue(cmdstr(cmd, '1 2'), '0\n')
    assert getattr(gcs, cmd)(1, '2') is False
    checksvr(gcs)


def test_get_list_args(gcs, cmd):
    """Arguments as lists."""
    PIDebug('enter test_get_2arg_{req_opt}__bool.test_get_list_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3 0'), '1\n')
    assert getattr(gcs, cmd)(['1', 3], [2, False]) is True
    checksvr(gcs)


def test_get_list_scalar_args(gcs, cmd):
    """Arguments as lists and scalars mixed."""
    PIDebug('enter test_get_2arg_{req_opt}__bool.test_get_list_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2'), '1\n')
    assert getattr(gcs, cmd)(['1'], 2) is True
    gcs.svr.queue(cmdstr(cmd, '1 0'), '1\n')
    assert getattr(gcs, cmd)(True, [False]) is True
    checksvr(gcs)


def test_get_dict_arg(gcs, cmd):
    """Arguments as dict."""
    PIDebug('enter test_get_2arg_{req_opt}__bool.test_get_dict_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3 0'), '1\n')
    assert getattr(gcs, cmd)({'1': 2, 3: False}) is True
    checksvr(gcs)


def test_different_list_sizes(gcs, cmd):
    """Arguments as lists with different sizes."""
    PIDebug('enter test_get_2arg_{req_opt}__bool.py.test_different_list_sizes(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1])
    checksvr(gcs)


def test_missing_args(gcs, cmd):
    """No arguments, not enough arguments, empty strings, lists and dicts."""
    PIDebug('enter test_get_2arg_{req_opt}__bool.test_missing_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)()
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([], [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None, [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({})
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
