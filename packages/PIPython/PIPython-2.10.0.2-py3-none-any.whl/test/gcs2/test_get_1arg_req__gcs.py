#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands that query GCS data with this signature: CMD req."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
__signature__ = 0xdeaac084e9169438911d4ea61f7d10ad

from pipython import PIDebug

# Unable to import 'ordereddict' pylint: disable=F0401
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import pytest

from test.tools import checksvr

CMDS = [
    'read_gcsdata',
]

ANSWER = '# REM C-884 \n' \
         '# \n' \
         '# VERSION = 1 \n' \
         '# TYPE = 1 \n' \
         '# SEPARATOR = 32 \n' \
         '# DIM = 4 \n' \
         '# SAMPLE_TIME = 0.100000 \n' \
         '# NDATA = 16 \n' \
         '# \n' \
         '# NAME0 = Commanded Position of Axis  AXIS:1 \n' \
         '# NAME1 = Actual Position of Axis  AXIS:1 \n' \
         '# NAME2 = Commanded Position of Axis  AXIS:TWO \n' \
         '# NAME3 = Actual Position of Axis  AXIS:TWO \n' \
         '# \n' \
         '# END_HEADER \n' \
         '1.0 2.0 3.0 4.0 \n' \
         '0.0469322 0.0468292 0.0469254 0.0468018 \n' \
         '0.1219345 0.1219070 0.1219276 0.1218933 \n' \
         '0.1969299 0.1969231 0.1969299 0.1969368 \n' \
         '0.2719322 0.2719391 0.2719322 0.2719185 \n' \
         '0.3469345 0.3469345 0.3469276 0.3469276 \n' \
         '0.4219368 0.4219437 0.4219299 0.4219368 \n' \
         '0.4969322 0.4969322 0.4969322 0.4969185 \n' \
         '0.5719345 0.5719345 0.5719276 0.5719345 \n' \
         '0.6469368 0.6469574 0.6469299 0.6469505 \n' \
         '0.7219322 0.7219597 0.7219322 0.7219116 \n' \
         '0.7969345 0.7969276 0.7969276 0.7969276 \n' \
         '0.8719368 0.8719299 0.8719299 0.8719437 \n' \
         '0.9469322 0.9469460 0.9469322 0.9469185 \n' \
         '0.9996460 0.9998039 0.9996460 0.9998108 \n' \
         '100034 100858 100034 100721\n'

HEADER = OrderedDict([(u'VERSION', 1),
                      (u'TYPE', 1),
                      (u'SEPARATOR', 32),
                      (u'DIM', 4),
                      (u'SAMPLE_TIME', 0.1),
                      (u'NDATA', 16),
                      (u'NAME0', 'Commanded Position of Axis  AXIS:1'),
                      (u'NAME1', 'Actual Position of Axis  AXIS:1'),
                      (u'NAME2', 'Commanded Position of Axis  AXIS:TWO'),
                      (u'NAME3', 'Actual Position of Axis  AXIS:TWO')])

DATA = [[1.0,
         0.0469322,
         0.1219345,
         0.1969299,
         0.2719322,
         0.3469345,
         0.4219368,
         0.4969322,
         0.5719345,
         0.6469368,
         0.7219322,
         0.7969345,
         0.8719368,
         0.9469322,
         0.999646,
         100034],
        [2.0,
         0.0468292,
         0.121907,
         0.1969231,
         0.2719391,
         0.3469345,
         0.4219437,
         0.4969322,
         0.5719345,
         0.6469574,
         0.7219597,
         0.7969276,
         0.8719299,
         0.946946,
         0.9998039,
         100858],
        [3.0,
         0.0469254,
         0.1219276,
         0.1969299,
         0.2719322,
         0.3469276,
         0.4219299,
         0.4969322,
         0.5719276,
         0.6469299,
         0.7219322,
         0.7969276,
         0.8719299,
         0.9469322,
         0.999646,
         100034],
        [4.0,
         0.0468018,
         0.1218933,
         0.1969368,
         0.2719185,
         0.3469276,
         0.4219368,
         0.4969185,
         0.5719345,
         0.6469505,
         0.7219116,
         0.7969276,
         0.8719437,
         0.9469185,
         0.9998108,
         100721]]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_get_scalar_args(gcs, cmd):
    """No tables given."""
    PIDebug('enter test_get_1arg_req__gcs.test_get_scalar_args(%s)', cmd)
    gcs.svr.queue('DRR?\n', ANSWER)
    assert HEADER == getattr(gcs, cmd)('DRR?')
    while gcs.bufstate is not True:
        pass
    assert DATA == gcs.bufdata
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_1arg_req__gcs.test_wrong_arg(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(['1', 2])
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 2)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)({1: 2})
    checksvr(gcs)


def test_missing_args(gcs, cmd):
    """No arguments, not enough arguments, empty strings, lists and dicts."""
    PIDebug('enter test_get_1arg_req__gcs.test_missing_args(%s)', cmd)
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
