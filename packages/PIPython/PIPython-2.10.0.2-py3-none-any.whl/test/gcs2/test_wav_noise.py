#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test wave noise command."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
# Too many statements (53/50) pylint: disable=R0915
__signature__ = 0xc02ef232c868514a4f45538d616e6cab

from pipython import PIDebug

import pytest

from test.tools import checksvr

CMDS = [
    'WAV_NOISE',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_set_scalar_args(gcs, cmd):
    """Scalar arguments."""
    PIDebug('enter test_wav_noise.test_set_scalar_args(%s)', cmd)
    wavetype = cmd.split('_')[1]
    gcs.svr.queue('WAV 1 & %s 40 2 3\n' % wavetype)
    getattr(gcs, cmd)('1', '&', 2.0, 3, 40)
    checksvr(gcs)


def test_wrong_argtype(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_wav_noise.test_wrong_argtype(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2.1, 3], [2, 3, 4], ['3', 'a', 5], ['5', 'a', 5], ['5', 'a', 5])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2, 3, 4, ['5', 'a', 5])
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
    PIDebug('enter test_wav_noise.test_set_list_scalar_args(%s)', cmd)
    wavetype = cmd.split('_')[1]
    gcs.svr.queue('WAV 1 & %s 40 2 3\n' % wavetype)
    gcs.svr.queue('WAV 1 & %s 40 2 3\n' % wavetype)
    getattr(gcs, cmd)('1', ['&'], 2.0, 3, 40)
    getattr(gcs, cmd)('1', '&', 2.0, [3], [40])
    checksvr(gcs)


def test_different_list_sizes(gcs, cmd):
    """Arguments as lists with different sizes."""
    PIDebug('enter test_wav_noise.test_different_list_sizes(%s)', cmd)
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
    PIDebug('enter test_wav_noise.test_missing_args(%s)', cmd)
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
