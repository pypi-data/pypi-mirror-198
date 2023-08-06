#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning a {string_int} with this signature: CMD."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0xcfb30a493b38c495bb016a7fce22fea2

from pipython import PIDebug

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'qTIO',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_no_arg(gcs, cmd):
    """No arguments."""
    PIDebug('enter test_get_0arg__{str_int}.test_no_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), 'foo=1 \nbar=2\n')
    assert OrderedDict([('foo', 1), ('bar', 2)]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_get_answer_with_spaces(gcs, cmd):
    """Arguments as lists."""
    PIDebug('enter test_get_0arg__{str_int}.test_get_answer_with_spaces(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '   foo \t=\t  1    \n  bar            =   2\n')
    assert OrderedDict([('foo', 1), ('bar', 2)]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_0arg__{str_int}.test_set_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1)
    checksvr(gcs)


def test_wrong_answer(gcs, cmd):
    """Controller sends wrong answer."""
    PIDebug('enter test_get_0arg__{str_int}.test_wrong_answer(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '1=a\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
