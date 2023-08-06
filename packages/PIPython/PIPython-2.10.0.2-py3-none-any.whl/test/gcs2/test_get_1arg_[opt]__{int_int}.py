#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning a dict of int/int with this signature: CMD [opt]."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0xf9f74a215a3193594db2db40ca1f05ec

from pipython import PIDebug

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'qATC',
    'qDRL',
    'qDTL',
    'qNAV',
    'qSGA',
    'qTAD',
    'qTGL',
    'qWGC',
    'qWGI',
    'qWGN',
    'qWGO',
    'qWMS',
    'qWSL',
    'qWTR',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_get_noargs(gcs, cmd):
    """No arguments. Will return converted "items". """
    PIDebug('enter test_get_1arg_[opt]__{int_int}.test_get_noargs(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '1=7 \n2=0 \n3=-18\n')
    assert OrderedDict([(1, 7), (2, 0), (3, -18)]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_get_scalar_args(gcs, cmd):
    """Scalar arguments. Will return original "items"."""
    PIDebug('enter test_get_1arg_[opt]__{int_int}.test_get_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1'), '1=7\n')
    assert OrderedDict([('1', 7)]) == getattr(gcs, cmd)('1')
    gcs.svr.queue(cmdstr(cmd, '1'), '1=-7\n')
    assert OrderedDict([(1, -7)]) == getattr(gcs, cmd)(1)
    checksvr(gcs)


def test_get_list_args(gcs, cmd):
    """Arguments as lists. Will return original "items"."""
    PIDebug('enter test_get_1arg_[opt]__{int_int}.test_get_list_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3'), '1=7 \n2=0 \n3=-18\n')
    assert OrderedDict([('1', 7), (2, 0), ('3', -18)]) == getattr(gcs, cmd)(['1', 2, '3'])
    checksvr(gcs)


def test_get_answer_with_spaces(gcs, cmd):
    """Arguments as lists."""
    PIDebug('enter test_get_1arg_[opt]__{int_int}.test_get_answer_with_spaces(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3'), '1 =7 \n2=  0 \n3  =   -18\n')
    assert OrderedDict([('1', 7), (2, 0), ('3', -18)]) == getattr(gcs, cmd)(['1', 2, '3'])
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_1arg_[opt]__{int_int}.test_set_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 1})
    checksvr(gcs)


def test_wrong_answer(gcs, cmd):
    """Controller sends wrong answer."""
    PIDebug('enter test_get_1arg_[opt]__{int_int}.test_wrong_answer(%s)', cmd)
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
