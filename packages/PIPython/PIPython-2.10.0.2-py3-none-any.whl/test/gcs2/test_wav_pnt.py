#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test wave pnt command."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
# Too many statements (53/50) pylint: disable=R0915
__signature__ = 0x9c2b649a8aefe187e60b2371a2dac425

from pipython import PIDebug

import pytest

from test.tools import checksvr

CMDS = [
    'WAV_PNT',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_set_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_wav_pnt.test_set_scalar_args(%s)', cmd)
    wavetype = cmd.split('_')[1]
    gcs.svr.queue('WAV 1 & %s 1 40 7\n' % wavetype)
    getattr(gcs, cmd)('1', 1, 40, '&', 7)
    checksvr(gcs)


def test_wrong_argtype(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_wav_pnt.test_wrong_argtype(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2.1, 3], [2, 3, 4], ['3', 'a', 5], ['5', 'a', 5], ['5', 'a', 5])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2.1, 3], [2, 3, 4], ['3', 'a', 5], ['5', 'a', 5], [4])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({'1': 2.1}, {2: 3}, {'3': 'a'}, {'3': 'a'}, {'3': 'a'})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({'1': 2.1}, {2: 3}, {'3': 'a'}, 4, 2)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2.1}, 1, 1, 4, 4)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2.1}, 1, 1, 4, 3)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2.1, 3], [2, 3, 4], ['3', 'a', 5], {4}, 5)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({'1': 2.1}, {2: 3}, {'3': 'a'}, {'3': 'a'}, {'r': 5})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2.1}, 1, 1, 4, 5)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, {1: 2.1}, 4, 4, 5)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 1, 2, {1: 2.1})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 1, 1, {1: 2.1}, 4)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, -3, 1, '', 2)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('', '', '', '', '')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None, None, None, 2, 3)
    checksvr(gcs)


def test_set_list_scalar_args(gcs, cmd):
    """Arguments as lists and scalars mixed."""
    PIDebug('enter test_wav_pnt.test_set_list_scalar_args(%s)', cmd)
    wavetype = cmd.split('_')[1]
    gcs.svr.queue('WAV 1 & %s 1 40 7\n' % wavetype)
    gcs.svr.queue('WAV 1 & %s 1 40 7\n' % wavetype)
    getattr(gcs, cmd)('1', [1], 40, '&', 7)
    getattr(gcs, cmd)('1', 1, 40, ['&'], [7])
    checksvr(gcs)
    gcs.svr.queue('WAV 1 & %s 1 40 7 8 9 10\n' % wavetype)
    gcs.svr.queue('WAV 1 & %s 1 40 7 8 9 10\n' % wavetype)
    getattr(gcs, cmd)('1', [1], 40, '&', [7, 8, 9, 10])
    getattr(gcs, cmd)('1', 1, 40, ['&'], [7, 8, 9, 10])
    checksvr(gcs)


def test_different_list_sizes(gcs, cmd):
    """Arguments as lists with different sizes."""
    PIDebug('enter test_wav_pnt.test_different_list_sizes(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1], [None, None], 4, 5)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1], [None, None], True, False)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2], [1], False, 5)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2], [3, 4], '3', '3')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2], [3, 4], [4], [3, 4])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2'], [1, 2], [3, 4], [4], 5)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1], [2], [None], True)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1], [2], None, None)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1], [2, 3], '2', 8)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1], [2, 3], 5, 4)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['2', '3'], [1, 2], [None], True, False)
    checksvr(gcs)


def test_missing_args(gcs, cmd):
    """No arguments, not enough arguments, empty strings, lists and dicts."""
    PIDebug('enter test_wav_pnt.test_missing_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('1', [], [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('1', [], [], [], [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('1', 2, [], '3', 3)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)('1', 2, [], 4)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({}, 2, {})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({}, 2, 3, {}, 4)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 5, 4)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([], [], [], 4)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([], [], [], [], [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([], [])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([], [], [], [], [4])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None, [], None, None, None)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 4)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1, 2, 3, 4])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([1], [2], [3], '')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None, None, None, '')
    with pytest.raises(TypeError):
        getattr(gcs, cmd)()
    with pytest.raises(TypeError):
        getattr(gcs, cmd)([])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({}, {}, {}, {}, {})
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({0: None})
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
