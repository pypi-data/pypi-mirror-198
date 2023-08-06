#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning a dict of int/str/any with this signature: CMD opt opt."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
__signature__ = 0xf2b595b3cc56dfa97953f2e9a7b8a7f8

from pipython import PIDebug

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'qWGS',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_get_no_args(gcs, cmd):
    """No arguments."""
    PIDebug('enter test_get_2arg_opt_opt__{int_{str_any}}.test_get_no_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '1 STATUS=0xA \n1 ITERATIONS=10 \n2 ERRORTYPE=foo \n3 ERRORINDEX=9\n')
    assert OrderedDict([(1, OrderedDict([('STATUS', 10), ('ITERATIONS', 10)])),
                        (2, OrderedDict([('ERRORTYPE', 'foo')])),
                        (3, OrderedDict([('ERRORINDEX', 9)]))]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_2arg_opt_opt__{int_{str_any}}.test_wrong_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, ['1', 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 3)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, {1: 2})
    checksvr(gcs)


def test_get_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_get_2arg_opt_opt__{int_{str_any}}.test_get_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1'), '1 STATUS=0xA \n1 ITERATIONS=10\n')
    gcs.svr.queue(cmdstr(cmd, '1'), '1 STATUS=0xA \n1 ITERATIONS=10\n')
    assert OrderedDict([(1, OrderedDict([('STATUS', 10), ('ITERATIONS', 10)]))]) == getattr(gcs, cmd)(1)
    assert OrderedDict([('1', OrderedDict([('STATUS', 10), ('ITERATIONS', 10)]))]) == getattr(gcs, cmd)('1')
    gcs.svr.queue(cmdstr(cmd, '1 STATUS'), '1 STATUS=0xA\n')
    assert OrderedDict([(1, OrderedDict([('STATUS', 10)]))]) == getattr(gcs, cmd)(1, 'STATUS')
    checksvr(gcs)


def test_get_answer_with_spaces(gcs, cmd):
    """Controller sends answer with too many spaces."""
    PIDebug('enter test_get_2arg_opt_opt__{int_{str_any}}.test_get_answer_with_spaces(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 STATUS'), '1                   STATUS=0xA\n')
    gcs.svr.queue(cmdstr(cmd, '1 STATUS'), '1 STATUS             =0xA\n')
    gcs.svr.queue(cmdstr(cmd, '1 STATUS'), '1 STATUS      =     0xA\n')
    gcs.svr.queue(cmdstr(cmd, '1 STATUS'), '       1     STATUS =     0xA\n')
    assert OrderedDict([(1, OrderedDict([('STATUS', 10)]))]) == getattr(gcs, cmd)(1, 'STATUS')
    assert OrderedDict([(1, OrderedDict([('STATUS', 10)]))]) == getattr(gcs, cmd)(1, 'STATUS')
    assert OrderedDict([(1, OrderedDict([('STATUS', 10)]))]) == getattr(gcs, cmd)(1, 'STATUS')
    assert OrderedDict([(1, OrderedDict([('STATUS', 10)]))]) == getattr(gcs, cmd)(1, 'STATUS')
    checksvr(gcs)


def test_wrong_answer(gcs, cmd):
    """Controller sends wrong answer."""
    PIDebug('enter test_get_2arg_opt_opt__{int_{str_any}}.test_wrong_answer(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '1.5 STATUS=0xA\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
