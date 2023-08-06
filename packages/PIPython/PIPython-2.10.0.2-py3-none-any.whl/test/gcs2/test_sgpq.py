#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test qSGP command."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0xa72616aa2521270acfa933a40f8dcf07

from pipython import PIDebug

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'qSGP',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_get_noargs(gcs, cmd):
    """No arguments. Will return converted "items"."""
    PIDebug('enter test_sgpq.test_get_noargs(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), 'a 1 b 2 3=1.23 \ncde 4 fgh 56 7=foo  \n8 9 10 11 12=1\n')
    assert (['a', 'cde', '8'], [1, 4, 9], ['b', 'fgh', '10'], [2, 56, 11], [3, 7, 12],
            [1.23, 'foo', 1]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_sgpq.test_wrong_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1, 2], 3, 4, 5, 6)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, [2, 3], 4, 5, 6)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, [3, 4], 5, 6)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 3, [4, 5], 6)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 3, 4, [5, 6])
    with pytest.raises(SystemError):
        getattr(gcs, cmd)(1, 2, 3)
    with pytest.raises(SystemError):
        getattr(gcs, cmd)(1)
    checksvr(gcs)


def test_get_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_sgpq.test_get_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, 'a 1 b 2 3'), 'a 1 b 2 3=1.23\n')
    gcs.svr.queue(cmdstr(cmd, 'a 1 b 2 3'), 'a 1 b 2 3=1.23\n')
    assert (['a'], [1], ['b'], [2], [3], [1.23]) == getattr(gcs, cmd)('a', 1, 'b', 2, '3')
    assert (['a'], [1], ['b'], [2], [3], [1.23]) == getattr(gcs, cmd)('a', '1', 'b', '2', 3)
    checksvr(gcs)


def test_get_list_args(gcs, cmd):
    """Arguments as lists."""
    PIDebug('enter test_sgpq.test_get_list_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, 'a 1 b 2 3 cde 4 fgh 56 7 8 9 10 11 12'),
                  'a 1 b 2 3=1.23 \ncde 4 fgh 56 7=foo \n8 9 10 11 12=1\n')
    gcs.svr.queue(cmdstr(cmd, 'a 1 b 2 3 cde 4 fgh 56 7 8 9 10 11 12'),
                  'a 1 b 2 3=1.23 \ncde 4 fgh 56 7=foo \n8 9 10 11 12=1\n')
    assert (['a', 'cde', '8'], [1, 4, 9], ['b', 'fgh', '10'], [2, 56, 11], [3, 7, 12], [1.23, 'foo', 1]) == \
           getattr(gcs, cmd)(['a', 'cde', '8'], [1, 4, 9], ['b', 'fgh', '10'], [2, 56, 11], [3, 7, 12])
    assert (['a', 'cde', '8'], [1, 4, 9], ['b', 'fgh', '10'], [2, 56, 11], [3, 7, 12], [1.23, 'foo', 1]) == \
           getattr(gcs, cmd)(['a', 'cde', 8], [1, 4, 9], ['b', 'fgh', 10], [2, 56, 11], [3, 7, 12])
    checksvr(gcs)


def test_get_answer_with_spaces(gcs, cmd):
    """Controller sends answer with too many spaces."""
    PIDebug('enter test_sgpq.test_get_answer_with_spaces(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, 'a 1 b 2 3'), '  a    1   b  2   3  =   1.23\n')
    assert (['a'], [1], ['b'], [2], [3], [1.23]) == getattr(gcs, cmd)('a', '1', 'b', '2', 3)
    checksvr(gcs)


def test_wrong_answer(gcs, cmd):
    """Controller sends wrong answer."""
    PIDebug('enter test_sgpq.test_wrong_answer(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), 'a 1 b 2 3=1.23 \ncde 4 fgh 56 =foo  \n8 9 10 11 12=1\n')
    with pytest.raises(IndexError):
        getattr(gcs, cmd)()
    gcs.svr.queue(cmdstr(cmd), 'a x b 2 3 7=1.23 \ncde 4 fgh 56 =foo  \n8 9 10 11 12=1\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
