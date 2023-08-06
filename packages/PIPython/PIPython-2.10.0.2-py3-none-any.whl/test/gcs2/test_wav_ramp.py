#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test wave ramp command."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
# Too many statements (53/50) pylint: disable=R0915
__signature__ = 0xb4113d67f27a5abca91be83363eee5d0

from pipython import PIDebug

import pytest

from test.tools import checksvr

CMDS = [
    'WAV_RAMP',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_set_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_wav_ramp.test_set_scalar_args(%s)', cmd)
    gcs.svr.queue('WAV 1 & %s 40 2 4 30 3 5 7\n' % 'RAMP')
    getattr(gcs, cmd)('1', 3, 30, '&', 7.0, 5.0, 2.0, 4, 40)
    checksvr(gcs)


def test_wrong_argtype(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_wav_ramp.test_wrong_argtype(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2.1, 3], [2, 3, 4], ['3', 'a', 5], ['5', 'a', 5], ['5', 'a', 5],
                          ['5', 'a', 5], ['5', 'a', 435], ['5', 'a', 53], ['5', 'a', 54])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 3, 4, ['5', 'a', 5], ['5', 'a', 5], 7, 8, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2.1, 3], [2, 3, 4], ['3', 'a', 5], ['5', 'a', 5], [4], -5, 7, 8, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({'1': 2.1}, {2: 3}, {'3': 'a'}, {'3': 'a'}, {'3': 'a'}, '4', 7, '8', 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({'1': 2.1}, {2: 3}, {'3': 'a'}, 4, 2, 6, -7, -8, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2.1}, 1, 1, 4, 4, 5, 0, 0, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, {1: 2.1}, 1, 1, 4, 3, 3, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2.1, 3], [2, 3, 4], ['3', 'a', 5], {'R': 4}, 5, {'t': 3}, '3', [3],
                          9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({'1': 2.1}, {2: 3}, {'3': 'a'}, {'3': 'a'}, {'r': 5}, {'t': 5}, {'r': 5},
                          {'t': 5}, {'t': 5})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2.1}, 1, 1, 4, 5, [4], '7', '8', 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, {1: 2.1}, 4, 4, 5, 6, [0], [0], 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 1, 2, {1: 2.1}, 5, {'z': 7}, {'t': 7}, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 1, 1, {1: 2.1}, 4, 5, 0, 8, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, -3, 1, '', 2, 6, '', None, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('', '', '', '', '', '', '', '', '')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None, None, None, 2, 3, 6, 0, 5, 9)
    checksvr(gcs)


def test_set_list_scalar_args(gcs, cmd):
    """Arguments as lists and scalars mixed."""
    PIDebug('enter test_wav_ramp.test_set_list_scalar_args(%s)',
            cmd)
    gcs.svr.queue('WAV 1 & %s 40 2 4 30 3 5 7\n' % 'RAMP')
    gcs.svr.queue('WAV 1 & %s 40 2 4 30 3 5 7\n' % 'RAMP')
    getattr(gcs, cmd)('1', 3, 30, ['&'], [7.0], [5.0], 2.0, 4, 40)
    getattr(gcs, cmd)('1', 3, 30, '&', 7.0, 5.0, 2.0, 4, [40])
    checksvr(gcs)


def test_different_list_sizes(gcs, cmd):
    """Arguments as lists with different sizes."""
    PIDebug(
        'enter test_wav_ramp.test_different_list_sizes(%s)',
        cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1], [None, None], 4, 5, 6, 7, 8, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1], [None, None], True, False, 6, 0, 0, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2], [1], False, 5, 4, 5, 4, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2], [3, 4], '3', '3', [5], 5, 6, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2], [3, 4], [4], [3, 4], 5, [], [], 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2], [3, 4], [4], 4, 5, '', '', 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1], [2], [None], True, 4, [6], [7], 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1], [2], None, None, 4, [5], [6], 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1], [2, 3], '2', 8, 5, '', True, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1], [2, 3], 5, 4, 5, True, False, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1, 2], [None], True, False, 5, 3, 4, 9)
    checksvr(gcs)


def test_missing_args(gcs, cmd):
    """No arguments, not enough arguments, empty strings, lists and dicts."""
    PIDebug('enter test_wav_ramp.test_missing_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('1', [], [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('1', [], [], [], [], [], [], [], [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('1', 2, [], '3', 3, 5, 7, 8, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('1', 2, 3, 4, 4, [], 4, 5, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({}, 2, {}, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({}, 2, 3, {}, 4, 6, 7, 8, 9, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, None, 5, 4, 5, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([], [], [], 4, 5, 9)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([], [], [], [], [], [], [], [], [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([], [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([], [], [], [], [4], 0, 3, 4)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None, [], None, None, None, None, None, None)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 4)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1, 2, 3, 4])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [2], [3], '', '', '')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None, None, None, '', {}, {})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)()
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({}, {}, {}, {}, {}, {}, {}, {}, {})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({0: None})
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
