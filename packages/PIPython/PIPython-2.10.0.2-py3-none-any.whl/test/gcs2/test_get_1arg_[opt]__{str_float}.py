#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning a dict of str/float with this signature: CMD [opt]."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0x16d718431b51add3992558c440c89caf

from pipython import PIDebug

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'GetPosStatus',
    'qACC',
    'qAOS',
    'qCAV',
    'qCCV',
    'qCMN',
    'qCMX',
    'qCTV',
    'qDEC',
    'qDFF',
    'qDFH',
    'qFPH',
    'qIMP',
    'qJOG',
    'qMOV',
    'qNLM',
    'qOAC',
    'qODC',
    'qPLM',
    'qPOS',
    'qSPI',
    'qSRA',
    'qSST',
    'qSTE',
    'qSVA',
    'qTCV',
    'qTMN',
    'qTMX',
    'qVEL',
    'qSMR',
    'qSMV',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_get_noargs(gcs, cmd):
    """No arguments. Will return converted "items". """
    PIDebug('enter test_get_1arg_[opt]__{str_float}.test_get_noargs(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '1=1.23 \n2=2.34 \n3=3.45\n')
    assert OrderedDict([('1', 1.23), ('2', 2.34), ('3', 3.45)]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_get_scalar_args(gcs, cmd):
    """Scalar arguments. Will return original "items"."""
    PIDebug('enter test_get_1arg_[opt]__{str_float}.test_get_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1'), '1=1.23\n')
    assert OrderedDict([('1', 1.23)]) == getattr(gcs, cmd)('1')
    gcs.svr.queue(cmdstr(cmd, '1'), '1=1.23\n')
    assert OrderedDict([(1, 1.23)]) == getattr(gcs, cmd)(1)
    checksvr(gcs)


def test_get_list_args(gcs, cmd):
    """Arguments as lists. Will return original "items"."""
    PIDebug('enter test_get_1arg_[opt]__{str_float}.test_get_list_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3'), '1=1.23 \n2=2.34 \n3=3.45\n')
    assert OrderedDict([('1', 1.23), (2, 2.34), ('3', 3.45)]) == getattr(gcs, cmd)(['1', 2, '3'])
    checksvr(gcs)


def test_get_answer_with_spaces(gcs, cmd):
    """Arguments as lists."""
    PIDebug('enter test_get_1arg_[opt]__{str_float}.test_get_answer_with_spaces(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 3'), '1 =1.23 \n2=  2.34 \n3  =   3.45\n')
    assert OrderedDict([('1', 1.23), (2, 2.34), ('3', 3.45)]) == getattr(gcs, cmd)(['1', 2, '3'])
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_1arg_[opt]__{str_float}.test_set_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 1})
    checksvr(gcs)


def test_wrong_answer(gcs, cmd):
    """Controller sends wrong answer."""
    PIDebug('enter test_get_1arg_[opt]__{str_float}.test_wrong_answer(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '1=a\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
