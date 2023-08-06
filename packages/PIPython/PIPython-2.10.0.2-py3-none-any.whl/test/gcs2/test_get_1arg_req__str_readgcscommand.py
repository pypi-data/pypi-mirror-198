#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test ReadGCSCommand()."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
__signature__ = 0xef6717666030d09631c7271e456ad996

from pipython import PIDebug

import pytest

from test.tools import checksvr

CMDS = [
    'ReadGCSCommand',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_get_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_get_1arg_req__str_readgcscommand.test_get_scalar_args(%s)', cmd)
    gcs.svr.queue('POS? 1 2 c\n', '1=7 \n2=8 \nc=9\n')
    assert '1=7 \n2=8 \nc=9\n' == getattr(gcs, cmd)('POS? 1 2 c\n')
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_1arg_req__str_readgcscommand.test_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2})
    checksvr(gcs)


def test_missing_args(gcs, cmd):
    """No arguments, not enough arguments, empty strings, lists and dicts."""
    PIDebug('enter test_get_1arg_req__str_readgcscommand.test_missing_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)()
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({})
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
