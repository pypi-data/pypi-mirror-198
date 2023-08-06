#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning a dict of str/float with this signature: CMD [req] [req]."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0xb218aad6611eee5e4f4f75c1613b1904

from pipython import PIDebug

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'qTRA',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_get_scalar_args(gcs, cmd):
    """Scalar arguments. Will return original "items"."""
    PIDebug('enter test_get_2arg_{req_opt}__{str_float}.test_get_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2'), '1=1.23\n')
    assert OrderedDict([('1', 1.23)]) == getattr(gcs, cmd)('1', 2)
    gcs.svr.queue(cmdstr(cmd, '1 2'), '1=1.23\n')
    assert OrderedDict([(1, 1.23)]) == getattr(gcs, cmd)(1, '2')
    checksvr(gcs)


def test_get_list_args(gcs, cmd):
    """Arguments as lists. Will return original "items"."""
    PIDebug('enter test_get_2arg_{req_opt}__{str_float}.test_get_list_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3 1'), '1=1.23 \n2=2.34\n')
    assert OrderedDict([('1', 1.23), (3, 2.34)]) == getattr(gcs, cmd)(['1', 3], ['2', True])
    checksvr(gcs)


def test_get_list_scalar_args(gcs, cmd):
    """Arguments as lists and scalars mixed."""
    PIDebug('enter test_get_2arg_{req_opt}__{str_float}.test_get_list_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2'), '1=1.23\n')
    assert OrderedDict([('1', 1.23)]) == getattr(gcs, cmd)(['1'], 2)
    gcs.svr.queue(cmdstr(cmd, '1 2'), '1=1.23\n')
    assert OrderedDict([(1, 1.23)]) == getattr(gcs, cmd)(True, [2])
    checksvr(gcs)


def test_get_dict_arg(gcs, cmd):
    """Arguments as dict."""
    PIDebug('enter test_get_2arg_{req_opt}__{str_float}.test_get_dict_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3 1'), '1=1.23 \n3=3.45\n')
    assert OrderedDict([(1, 1.23), ('3', 3.45)]) == getattr(gcs, cmd)({True: 2, '3': True})
    checksvr(gcs)


def test_different_list_sizes(gcs, cmd):
    """Arguments as lists with different sizes."""
    PIDebug('enter test_get_2arg_{req_opt}__{str_float}.py.test_different_list_sizes(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1])
    checksvr(gcs)


def test_get_answer_with_spaces(gcs, cmd):
    """Arguments as lists."""
    PIDebug('enter test_get_2arg_{req_opt}__{str_float}.test_get_answer_with_spaces(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3 1'), '  1    =    1.23       \n     3   =     3.45\n')
    assert OrderedDict([(1, 1.23), ('3', 3.45)]) == getattr(gcs, cmd)({True: 2, '3': True})
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_2arg_{req_opt}__{str_float}.test_set_wrong_arg(%s)', cmd)
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


def test_wrong_answer(gcs, cmd):
    """Controller sends wrong answer."""
    PIDebug('enter test_get_2arg_{req_opt}__{str_float}.test_wrong_answer(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2'), '1=1.q3\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)('1', 2)
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
