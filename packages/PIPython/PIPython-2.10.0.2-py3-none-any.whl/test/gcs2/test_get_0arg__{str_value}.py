#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning a {string_value} with this signature: CMD."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0xaed9fca75a4f58f89e5930a78b5dc522

from pipython import PIDebug

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_no_arg(gcs, cmd):
    """No arguments."""
    PIDebug('enter test_get_0arg__{str_value}.test_no_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), 'foo=1 \nbar=2.1 \negg=foo\n')
    assert OrderedDict([('foo', 1), ('bar', 2.1), ('egg', 'foo')]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_get_answer_with_spaces(gcs, cmd):
    """Arguments as lists."""
    PIDebug('enter test_get_0arg__{str_value}.test_get_answer_with_spaces(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), 'foo  =        1 \nbar=       2.1 \negg  =      foo\n')
    assert OrderedDict([('foo', 1), ('bar', 2.1), ('egg', 'foo')]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_0arg__{str_value}.test_set_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1)
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
