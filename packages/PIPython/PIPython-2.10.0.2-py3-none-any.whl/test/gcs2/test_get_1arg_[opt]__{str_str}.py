#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning a dict of str/str with this signature: CMD [opt]."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0x17bd69d3971ff6eeaf0aca1116f1e528

from pipython import PIDebug

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'qCST',
    'qDIA',
    'qFRC',
    'qIFC',
    'qIFS',
    'qKEN',
    'qKET',
    'qKLN',
    'qMAS',
    'qPUN',
    'qVAR',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_get_noargs(gcs, cmd):
    """No arguments. Will return converted "items". """
    PIDebug('enter test_get_1arg_[opt]__{str_str}.test_get_noargs(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '1=7 \n2=b \n3=-18\n')
    assert OrderedDict([('1', '7'), ('2', 'b'), ('3', '-18')]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_get_scalar_args(gcs, cmd):
    """Scalar arguments. Will return original "items"."""
    PIDebug('enter test_get_1arg_[opt]__{str_str}.test_get_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1'), '1=7\n')
    assert OrderedDict([('1', '7')]) == getattr(gcs, cmd)('1')
    gcs.svr.queue(cmdstr(cmd, '1'), '1=-7\n')
    assert OrderedDict([(1, '-7')]) == getattr(gcs, cmd)(1)
    checksvr(gcs)


def test_get_list_args(gcs, cmd):
    """Arguments as lists. Will return original "items"."""
    PIDebug('enter test_get_1arg_[opt]__{str_str}.test_get_list_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3'), '1=a7c \n2=bb0 \n3=x-d1g8\n')
    assert OrderedDict([('1', 'a7c'), (2, 'bb0'), ('3', 'x-d1g8')]) == getattr(gcs, cmd)(
        ['1', 2, '3'])
    checksvr(gcs)


def test_get_answer_with_spaces(gcs, cmd):
    """Arguments as lists."""
    PIDebug('enter test_get_1arg_[opt]__{str_str}.test_get_answer_with_spaces(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3'), '1 =7 \n2=  0 \n3  =   -18\n')
    assert OrderedDict([('1', '7'), (2, '0'), ('3', '-18')]) == getattr(gcs, cmd)(['1', 2, '3'])
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_1arg_[opt]__{str_str}.test_set_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 1})
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
