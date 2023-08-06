#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning a dict of int/[int, str] with this signature: CMD [opt]."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0xab8714b511009e82a6d624d6a4daaf27

from pipython import PIDebug

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'qDRC',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_get_noargs(gcs, cmd):
    """No arguments. Will return converted "items". """
    PIDebug('enter test_get_1arg_[opt]__{int_[str_int]}.test_get_noargs(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '1=foo 2 \n4=bar 5 \n7=egg 8\n')
    assert OrderedDict([(1, ['foo', 2]), (4, ['bar', 5]), (7, ['egg', 8])]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_1arg_[opt]__{int_[str_int]}.test_wrong_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, {1: 2})
    checksvr(gcs)


def test_get_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_get_1arg_[opt]__{int_[str_int]}.test_get_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1'), '1=foo 2\n')
    gcs.svr.queue(cmdstr(cmd, '1'), '1=foo 2\n')
    assert OrderedDict([('1', ['foo', 2])]) == getattr(gcs, cmd)('1')
    assert OrderedDict([(1, ['foo', 2])]) == getattr(gcs, cmd)(1)
    checksvr(gcs)


def test_get_list_args(gcs, cmd):
    """Arguments as list."""
    PIDebug('enter test_get_1arg_[opt]__{int_[str_int]}.test_get_list_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 4'), '1=foo 2 \n4=bar 5\n')
    gcs.svr.queue(cmdstr(cmd, '1 4'), '1=foo 2 \n4=bar 5\n')
    assert OrderedDict([('1', ['foo', 2]), (4, ['bar', 5])]) == getattr(gcs, cmd)(['1', 4])
    assert OrderedDict([(1, ['foo', 2]), ('4', ['bar', 5])]) == getattr(gcs, cmd)([1, '4'])
    checksvr(gcs)


def test_get_answer_with_spaces(gcs, cmd):
    """Controller sends answer with too many spaces."""
    PIDebug('enter test_get_1arg_[opt]__{int_[str_int]}.test_get_answer_with_spaces(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '  1\t=\tfoo\t  2    \n 4           =  bar      5   \n  7  =  egg   8\n')
    assert OrderedDict([(1, ['foo', 2]), (4, ['bar', 5]), (7, ['egg', 8])]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_answer(gcs, cmd):
    """Controller sends wrong answer."""
    PIDebug('enter test_get_1arg_[opt]__{int_[str_int]}.test_wrong_answer(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '1=2 1.1\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd), '1.5=2 1\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
