#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test setter commands with this signature: CMD {req_opt}."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0x766c55df3a15f60e8862984ea65562f4

from collections import OrderedDict
from pipython import PIDebug

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'ACC',
    'AOS',
    'ATC',
    'BRA',
    'CMO',
    'CPY',
    'CST',
    'CTR',
    'CTV',
    'DCO',
    'DEC',
    'DFF',
    'DIO',
    'DMOV',
    'EAX',
    'EGE',
    'FRP',
    'HIN',
    'IFC',
    'IMP',
    'JOG',
    'JON',
    'KCP',
    'KLN',
    'MAS',
    'MOV',
    'MRT',
    'MRW',
    'MVE',
    'MVR',
    'MVT',
    'NAV',
    'NLM',
    'OAC',
    'OAD',
    'ODC',
    'OMA',
    'OMR',
    'ONL',
    'OSM',
    'OVL',
    'PLM',
    'POS',
    'PUN',
    'RNP',
    'RON',
    'SAI',
    'SGA',
    'SMO',
    'SPI',
    'SRA',
    'SSA',
    'SSL',
    'SST',
    'STE',
    'SVA',
    'SVO',
    'SVR',
    'TGA',
    'TRI',
    'TRO',
    'TSP',
    'VAR',
    'VCO',
    'VEL',
    'VMA',
    'VMI',
    'VOL',
    'WGC',
    'WGO',
    'WMS',
    'WOS',
    'WSL',
    'POL',
    'SMV',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_set_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_set_2arg_{req_opt}.py.test_set_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2.34'))
    getattr(gcs, cmd)('1', 2.34)
    gcs.svr.queue(cmdstr(cmd, '0 2.34'))
    getattr(gcs, cmd)(False, '2.34')
    gcs.svr.queue(cmdstr(cmd, 'b a'))
    getattr(gcs, cmd)('b', 'a')
    checksvr(gcs)


def test_set_dict_arg(gcs, cmd):
    """Arguments as dict."""
    PIDebug('enter test_set_2arg_{req_opt}.py.test_set_dict_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2.34 2 abc 3 1'))
    getattr(gcs, cmd)(OrderedDict([('1', 2.34), (2, 'abc'), ('3', True)]))
    checksvr(gcs)


def test_set_list_args(gcs, cmd):
    """Arguments as lists."""
    PIDebug('enter test_set_2arg_{req_opt}.py.test_set_list_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2.34 2 4.56 3 6.78'))
    getattr(gcs, cmd)(['1', 2, '3'], [2.34, 4.56, '6.78'])
    gcs.svr.queue(cmdstr(cmd, '1 a'))
    getattr(gcs, cmd)(['1'], ['a'])
    checksvr(gcs)


def test_set_list_scalar_args(gcs, cmd):
    """Arguments as lists and scalars mixed."""
    PIDebug('enter test_set_2arg_{req_opt}.py.test_set_list_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2.34'))
    getattr(gcs, cmd)(['1'], 2.34)
    gcs.svr.queue(cmdstr(cmd, '1 2.34'))
    getattr(gcs, cmd)([1], '2.34')
    gcs.svr.queue(cmdstr(cmd, '1 2.34'))
    getattr(gcs, cmd)('1', [2.34])
    gcs.svr.queue(cmdstr(cmd, '1 2.34'))
    getattr(gcs, cmd)(1, ['2.34'])
    checksvr(gcs)


def test_different_list_sizes(gcs, cmd):
    """Arguments as lists with different sizes."""
    PIDebug('enter test_set_2arg_{req_opt}.py.test_different_list_sizes(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1])
    checksvr(gcs)


def test_missing_args(gcs, cmd):
    """No arguments, not enough arguments, empty strings, lists and dicts."""
    PIDebug('enter test_set_2arg_{req_opt}.py.test_missing_args(%s)', cmd)
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


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
