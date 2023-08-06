#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands that query GCS data with this signature: CMD opt opt [opt]."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
# Invalid module name pylint: disable=C0103
__signature__ = 0xa679c6be5424a433b821b13b34feca8d

from pipython import PIDebug

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import pytest
from test.tools import checksvr, cmdstr, GCSRaise
from pipython import gcserror

CMDS = [
    'qJLT',
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

HEADERONLY = '# REM C-884 \n' \
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
             '# END_HEADER \n'

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


def test_get_noargs(gcs, cmd):
    """No arguments."""
    PIDebug('enter test_get_4arg_opt_opt_[opt]_[opt]__gcs.test_get_noargs(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), ANSWER)
    assert HEADER == getattr(gcs, cmd)()
    while gcs.bufstate is not True:
        pass
    assert DATA == gcs.bufdata
    checksvr(gcs)


def test_wrong_args(gcs, cmd):
    """Wrong argument sizes and/or types."""
    PIDebug('enter test_get_4arg_opt_opt_[opt]_[opt]__gcs.test_wrong_args(%s)', cmd)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None, 1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None, None, 1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(None, None, None, 1)
    with pytest.raises(TypeError):
        getattr(gcs, cmd)(1, 1, [1], [1, 2])
    checksvr(gcs)


def test_get_scalar_args(gcs, cmd):
    """No rectables given."""
    PIDebug('enter test_get_4arg_opt_opt_[opt]_[opt]__gcs.test_get_scalar_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 16'), ANSWER)
    assert HEADER == getattr(gcs, cmd)(offset=1, numvalues=16)
    while gcs.bufstate is not True:
        pass
    assert DATA == gcs.bufdata
    gcs.svr.queue(cmdstr(cmd, '1 -1'), ANSWER)
    assert HEADER == getattr(gcs, cmd)(offset=1, numvalues=-1)
    while gcs.bufstate is not True:
        pass
    assert DATA == gcs.bufdata
    checksvr(gcs)


def test_get_list_args(gcs, cmd):
    """With rectables."""
    PIDebug('enter test_get_4arg_opt_opt_[opt]_[opt]__gcs.test_get_list_args(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 16 1 4 2 5 3 6 4 7'), ANSWER)
    assert HEADER == getattr(gcs, cmd)(1, 16, [1, 2, 3, 4], [4, 5, 6, 7])
    while gcs.bufstate is not True:
        pass
    assert DATA == gcs.bufdata
    checksvr(gcs)


def test_too_many_datasets(gcs, cmd):
    """Device returns more lines than expected."""
    PIDebug('enter test_get_4arg_opt_opt_[opt]_[opt]__gcs.test_too_many_datasets(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 15'), ANSWER)
    with GCSRaise(gcserror.E_1089_PI_TOO_MANY_GCS_DATA):
        assert HEADER == getattr(gcs, cmd)(offset=1, numvalues=15)
        while gcs.bufstate is not True:
            pass
    assert DATA == gcs.bufdata
    checksvr(gcs)


def test_too_few_datasets(gcs, cmd):
    """Device returns less lines than expected."""
    PIDebug('enter test_get_4arg_opt_opt_[opt]_[opt]__gcs.test_too_few_datasets(%s)', cmd)
    last_line_removed = ''.join(ANSWER.splitlines(True)[:-1])[:-2] + '\n'
    data = []
    for i in range(len(DATA)):
        data.append(DATA[i][:-1])
    gcs.svr.queue(cmdstr(cmd, '1 16'), last_line_removed)
    with GCSRaise(gcserror.E_1088_PI_TOO_FEW_GCS_DATA):
        assert HEADER == getattr(gcs, cmd)(offset=1, numvalues=16)
        while gcs.bufstate is not True:
            pass
    assert data == gcs.bufdata
    checksvr(gcs)


def test_invalid_number(gcs, cmd):
    """There is an invalid character in the last line of the answer."""
    PIDebug('enter test_get_4arg_opt_opt_[opt]_[opt]__gcs.test_invalid_number(%s)', cmd)
    answer = ANSWER.replace('100858', '1a0858')
    data = []
    for i in range(len(DATA)):
        data.append(DATA[i][:-1])
    gcs.svr.queue(cmdstr(cmd, '1 16'), answer)
    with GCSRaise(gcserror.E_1004_PI_UNEXPECTED_RESPONSE):
        assert HEADER == getattr(gcs, cmd)(offset=1, numvalues=16)
        while gcs.bufstate is not True:
            pass
    assert data == gcs.bufdata
    checksvr(gcs)


def test_missing_number(gcs, cmd):
    """One value is missing in the last line of the answer."""
    PIDebug('enter test_get_4arg_opt_opt_[opt]_[opt]__gcs.test_missing_number(%s)', cmd)
    answer = ANSWER.replace('100858 ', '')
    data = []
    for i in range(len(DATA)):
        data.append(DATA[i][:-1])
    gcs.svr.queue(cmdstr(cmd, '1 16'), answer)
    with GCSRaise(gcserror.E_1004_PI_UNEXPECTED_RESPONSE):
        assert HEADER == getattr(gcs, cmd)(offset=1, numvalues=16)
        while gcs.bufstate is not True:
            pass
    assert data == gcs.bufdata
    checksvr(gcs)


def test_no_answer(gcs, cmd):
    """Device returns only a linefeed."""
    PIDebug('enter test_get_4arg_opt_opt_[opt]_[opt]__gcs.test_no_answer(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 16'), '\n')
    gcs.svr.queue('ERR?\n', '26\n')
    with GCSRaise(gcserror.E26_PI_CNTR_MISSING_PARAM):
        assert HEADER == getattr(gcs, cmd)(offset=1, numvalues=16)
        while gcs.bufstate is not True:
            pass
    assert [] == gcs.bufdata
    gcs.svr.queue(cmdstr(cmd, '1 16'), '\n')
    gcs.svr.queue('ERR?\n', '0\n')
    with GCSRaise(gcserror.E_1004_PI_UNEXPECTED_RESPONSE):
        assert HEADER == getattr(gcs, cmd)(offset=1, numvalues=16)
        while gcs.bufstate is not True:
            pass
    assert [] == gcs.bufdata
    checksvr(gcs)


def test_header_lf(gcs, cmd):
    """Device returns only the header and a linefeed. Expect no exception, no data."""
    PIDebug('enter test_get_4arg_opt_opt_[opt]_[opt]__gcs.test_header_lf(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), HEADERONLY + '\n')
    assert HEADER == getattr(gcs, cmd)()
    timeout = gcs.timeout
    gcs.timeout = 100
    while gcs.bufstate is not True:
        pass
    assert [] == gcs.bufdata
    checksvr(gcs)
    gcs.timeout = timeout


def test_header_only(gcs, cmd):
    """Device returns only the header. Expect no exception, empty data."""
    PIDebug('enter test_get_4arg_opt_opt_[opt]_[opt]__gcs.test_header_only(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd), HEADERONLY.rstrip() + '\n')
    assert HEADER == getattr(gcs, cmd)()
    timeout = gcs.timeout
    gcs.timeout = 100
    while gcs.bufstate is not True:
        pass
    checksvr(gcs)
    gcs.timeout = timeout


def test_no_endofmessage(gcs, cmd):
    """Device returns answer with a " \n" at the end. Expect exception, data can be invalid."""
    PIDebug('enter test_get_4arg_opt_opt_[opt]_[opt]__gcs.test_no_endofmessage(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 16'), ANSWER[:-1] + ' \n')
    timeout = gcs.timeout
    gcs.timeout = 100
    with GCSRaise((gcserror.COM_TIMEOUT__7, gcserror.PI_GCS_DATA_READ_ERROR__1090)):
        assert HEADER == getattr(gcs, cmd)(offset=1, numvalues=16)
        while gcs.bufstate is not True:
            pass
    checksvr(gcs)
    gcs.svr.delay = 0
    gcs.timeout = timeout


def _test_timeout(gcs, cmd):
    """Device sends data too slow. Expect exception, data can be invalid."""
    PIDebug('enter test_get_4arg_opt_opt_[opt]_[opt]__gcs.test_timeout(%s)', cmd)
    gcs.svr.delay = 10
    gcs.svr.queue(cmdstr(cmd, '1 16'), ANSWER)
    assert HEADER == getattr(gcs, cmd)(offset=1, numvalues=16)
    timeout = gcs.timeout
    gcs.timeout = 1
    with GCSRaise(gcserror.COM_TIMEOUT__7):
        while gcs.bufstate is not True:
            pass
    gcs.timeout = timeout
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
