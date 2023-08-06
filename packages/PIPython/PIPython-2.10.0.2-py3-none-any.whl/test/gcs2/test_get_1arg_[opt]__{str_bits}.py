#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning a dict of str/bool with this signature: CMD."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0xd5a63b6adbf322a48e653b55fcb8be0f

from pipython import PIDebug

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'HasPosChanged',
    'IsMoving',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_no_args(gcs, cmd):
    """No arguments. Will return converted "items". """
    PIDebug('enter test_get_1arg_[opt]__{str_bits}.test_no_args(%s)', cmd)
    gcs.allaxes = ('1', '2', '3', '4')
    gcs.svr.queue(cmdstr(cmd), 'B\n')
    assert OrderedDict([('1', True), ('2', True), ('3', False), ('4', True)]) == getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd), '4\n')
    assert OrderedDict([('1', False), ('2', False), ('3', True), ('4', False)]) == getattr(gcs, cmd)()
    del gcs.axes
    checksvr(gcs)


def test_get_scalar_args(gcs, cmd):
    """Scalar arguments. Will return original "items"."""
    PIDebug('enter test_get_1arg_[opt]__{str_bits}.test_get_scalar_args(%s)', cmd)
    gcs.allaxes = ('1', '2', '3', '4')
    gcs.svr.queue(cmdstr(cmd), 'B\n')
    gcs.svr.queue(cmdstr(cmd), 'B\n')
    gcs.svr.queue(cmdstr(cmd), 'B\n')
    gcs.svr.queue(cmdstr(cmd), 'B\n')
    assert OrderedDict([(1, True)]) == getattr(gcs, cmd)(1)
    assert OrderedDict([(2, True)]) == getattr(gcs, cmd)(2)
    assert OrderedDict([(3, False)]) == getattr(gcs, cmd)(3)
    assert OrderedDict([(4, True)]) == getattr(gcs, cmd)(4)
    gcs.svr.queue(cmdstr(cmd), '0xB\n')
    gcs.svr.queue(cmdstr(cmd), '0xB\n')
    gcs.svr.queue(cmdstr(cmd), '0xB\n')
    gcs.svr.queue(cmdstr(cmd), '0xB\n')
    assert OrderedDict([(1, True)]) == getattr(gcs, cmd)(1)
    assert OrderedDict([(2, True)]) == getattr(gcs, cmd)(2)
    assert OrderedDict([(3, False)]) == getattr(gcs, cmd)(3)
    assert OrderedDict([(4, True)]) == getattr(gcs, cmd)(4)
    gcs.svr.queue(cmdstr(cmd), '4\n')
    gcs.svr.queue(cmdstr(cmd), '4\n')
    gcs.svr.queue(cmdstr(cmd), '4\n')
    gcs.svr.queue(cmdstr(cmd), '4\n')
    assert OrderedDict([('1', False)]) == getattr(gcs, cmd)('1')
    assert OrderedDict([('2', False)]) == getattr(gcs, cmd)('2')
    assert OrderedDict([('3', True)]) == getattr(gcs, cmd)('3')
    assert OrderedDict([('4', False)]) == getattr(gcs, cmd)('4')
    del gcs.axes
    checksvr(gcs)


def test_get_list_args(gcs, cmd):
    """Arguments as lists. Will return original "items"."""
    PIDebug('enter test_get_1arg_[opt]__{str_bits}.test_get_list_args(%s)', cmd)
    gcs.allaxes = ('1', '2', '3', '4')
    gcs.svr.queue(cmdstr(cmd), 'B\n')
    assert OrderedDict([(1, True), (2, True), ('3', False), (4, True)]) == getattr(gcs, cmd)([1, 2, '3', 4])
    gcs.svr.queue(cmdstr(cmd), '4\n')
    assert OrderedDict([(1, False), (2, False), ('3', True), ('4', False)]) == getattr(gcs, cmd)((1, 2, '3', '4'))
    del gcs.axes
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_1arg_[opt]__{str_bits}.test_set_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 1})
    checksvr(gcs)


def test_wrong_answer(gcs, cmd):
    """Controller sends wrong answer."""
    PIDebug('enter test_get_1arg_[opt]__{str_bits}.test_wrong_answer(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), 'a=-7\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd), '1=a\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
