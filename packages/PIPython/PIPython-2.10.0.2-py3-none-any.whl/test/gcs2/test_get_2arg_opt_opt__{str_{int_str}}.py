#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning a dict of str/int/str with this signature: CMD req opt."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0xb9f160bdbd2a711c0458414bae38d34e

from pipython import PIDebug

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import pytest

from test.tools import checksvr, cmdstr

CMDS = [
    'qFRR',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_no_args(gcs, cmd):
    """No arguments."""
    PIDebug('enter test_get_2arg_opt_opt__{str_{int_str}}.test_no_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '1 2=1.23 \n1 3=4.56 \n1 5=7.89\n')
    assert OrderedDict([('1', OrderedDict([(2, '1.23'), (3, '4.56'), (5, '7.89')]))]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_2arg_opt_opt__{str_{int_str}}.test_wrong_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, ['1', 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, {1: 2})
    checksvr(gcs)


def test_get_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_get_2arg_opt_opt__{str_{int_str}}.test_get_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2'), '1 2=1.23\n')
    gcs.svr.queue(cmdstr(cmd, '1 2'), '1 2=1.23\n')
    assert OrderedDict([('1', OrderedDict([('2', '1.23')]))]) == getattr(gcs, cmd)('1', '2')
    assert OrderedDict([(1, OrderedDict([(2, '1.23')]))]) == getattr(gcs, cmd)(1, 2)
    checksvr(gcs)


def test_get_list_args(gcs, cmd):
    """List arguments."""
    PIDebug('enter test_get_2arg_opt_opt__{str_{int_str}}.test_get_list_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 2 1 3 1 5'), '1 2=1.23 \n1 3=4.56 \n1 5=7.89\n')
    gcs.svr.queue(cmdstr(cmd, '1 2 1 3 1 5'), '1 2=1.23 \n1 3=4.56 \n1 5=7.89\n')
    assert OrderedDict([('1', OrderedDict([(2, '1.23'), (3, '4.56'),
                                           (5, '7.89')]))]) == getattr(gcs, cmd)(['1', '1', '1'], [2, 3, 5])
    assert OrderedDict([(1, OrderedDict([(2, '1.23'), (3, '4.56'),
                                         (5, '7.89')]))]) == getattr(gcs, cmd)([1, 1, 1], [2, 3, 5])
    checksvr(gcs)


def test_hexapod_answer(gcs, cmd):
    """Real answer from hexapod controller."""
    PIDebug('enter test_get_2arg_opt_opt__{str_{int_str}}.test_hexapod_answer(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), 'TEST3 1 = 0 \n'
                               'TEST3 2 = 0.971584 \n'
                               'TEST3 3 = 0. 0. \n'
                               'TEST3 4 = TEST3 X 0.100000 Z 0.100000 L 1. A 5 F 40. V 0.050000 '
                               'MP1 0. MP2 0. TT 0 CM 2 MIIL 0. MAIL 10. ST 0 \n'
                               'TEST3 5 = -2.017028 \nTEST3 6 = 0.\n')
    assert OrderedDict([('TEST3', OrderedDict([(1, [u'0']),
                                               (2, [u'0.971584']),
                                               (3, [u'0.', u'0.']),
                                               (4, [u'TEST3', u'X', u'0.100000', u'Z', u'0.100000', u'L', u'1.',
                                                    u'A', u'5', u'F', u'40.', u'V', u'0.050000',
                                                    u'MP1', u'0.', u'MP2', u'0.', u'TT', u'0', u'CM', u'2',
                                                    u'MIIL', u'0.', u'MAIL', u'10.', u'ST', u'0']),
                                               (5, [u'-2.017028']),
                                               (6, [u'0.'])]))]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_hexapod_answer_tuple_arg(gcs, cmd):
    """Real answer of one line from hexapod controller with tuple as argument."""
    PIDebug('enter test_get_2arg_opt_opt__{str_{int_str}}.test_hexapod_answer_tuple_arg(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, 'TEST3 1'), 'TEST3 1 = 0\n')
    assert OrderedDict([('TEST3', OrderedDict([(1, u'0')]))]) == getattr(gcs, cmd)(('TEST3',), 1)
    checksvr(gcs)


def test_get_answer_with_spaces(gcs, cmd):
    """Controller sends answer with too many spaces."""
    PIDebug('enter test_get_2arg_opt_opt__{str_{int_str}}.test_get_answer_with_spaces(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '1           2=1.23\n')
    gcs.svr.queue(cmdstr(cmd), '1   2      =1.23\n')
    gcs.svr.queue(cmdstr(cmd), '1   2  =        1.23\n')
    gcs.svr.queue(cmdstr(cmd), '     1   2  =   1.23\n')
    assert OrderedDict([('1', OrderedDict([(2, '1.23')]))]) == getattr(gcs, cmd)()
    assert OrderedDict([('1', OrderedDict([(2, '1.23')]))]) == getattr(gcs, cmd)()
    assert OrderedDict([('1', OrderedDict([(2, '1.23')]))]) == getattr(gcs, cmd)()
    assert OrderedDict([('1', OrderedDict([(2, '1.23')]))]) == getattr(gcs, cmd)()
    checksvr(gcs)


def test_wrong_answer(gcs, cmd):
    """Controller sends wrong answer."""
    PIDebug('enter test_get_2arg_opt_opt__{str_{int_str}}.test_wrong_answer(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), '1 2.5=1.23\n')
    with pytest.raises(ValueError):
        getattr(gcs, cmd)()
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
