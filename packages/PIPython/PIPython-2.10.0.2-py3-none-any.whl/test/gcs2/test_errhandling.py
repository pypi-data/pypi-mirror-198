#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test error handling properties."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
__signature__ = 0xa83763ea484476581bce073795c7ef98

from pipython import PIDebug

from pipython import GCSError, gcserror
from test.tools import checksvr, GCSRaise


def test_errcheck_setcmd(gcs):
    """Test errcheck property."""
    PIDebug('enter test_errhandling.test_errcheck_setcmd()')
    gcs.errcheck = True
    gcs.svr.queue('MOV 1 1\n')
    gcs.svr.queue('ERR?\n', '0\n')
    gcs.MOV(1, 1)
    gcs.errcheck = False
    gcs.svr.queue('MOV 1 1\n')
    gcs.MOV(1, 1)
    checksvr(gcs)


def test_errcheck_getcmd(gcs):
    """Test errcheck property."""
    PIDebug('enter test_errhandling.test_errcheck_getcmd()')
    gcs.errcheck = True
    gcs.svr.queue('POS? 1\n', '1=2\n')
    gcs.svr.queue('ERR?\n', '0\n')
    assert {1: 2.0} == gcs.qPOS(1)
    gcs.errcheck = False
    gcs.svr.queue('POS? 1\n', '1=2\n')
    assert {1: 2.0} == gcs.qPOS(1)
    checksvr(gcs)


def test_raise_gcserr(gcs):
    """Raise GCS Error."""
    PIDebug('enter test_errhandling.test_raise_gcserr()')
    gcs.errcheck = True
    gcs.svr.queue('MOV 1 1\n')
    gcs.svr.queue('ERR?\n', '37\n')
    with GCSRaise(37):
        gcs.MOV(1, 1)
    gcs.svr.queue('POS? 1\n', '1=2\n')
    gcs.svr.queue('ERR?\n', '-28\n')
    with GCSRaise(-28):
        gcs.qPOS(1)
    gcs.errcheck = False
    checksvr(gcs)


def test_embederr_setcmd(gcs):
    """Test embederr property."""
    PIDebug('enter test_errhandling.test_embederr_setcmd()')
    gcs.errcheck = True
    gcs.embederr = True
    gcs.svr.queue('MOV 1 1\n')
    gcs.svr.queue('ERR?\n', '0\n')
    gcs.MOV(1, 1)
    gcs.embederr = False
    gcs.svr.queue('MOV 1 1\n')
    gcs.svr.queue('ERR?\n', '0\n')
    gcs.MOV(1, 1)
    gcs.errcheck = False
    checksvr(gcs)


def test_embederr_getcmd(gcs):
    """Test embederr property."""
    PIDebug('enter test_errhandling.test_embederr_getcmd()')
    gcs.errcheck = True
    gcs.embederr = True
    gcs.svr.queue('POS? 1\n', '1=2\n')
    gcs.svr.queue('ERR?\n', '0\n')
    assert {1: 2.0} == gcs.qPOS(1)
    gcs.embederr = False
    gcs.svr.queue('POS? 1\n', '1=2\n')
    gcs.svr.queue('ERR?\n', '0\n')
    assert {1: 2.0} == gcs.qPOS(1)
    gcs.errcheck = False
    checksvr(gcs)


def test_gcserror_methods(gcs):
    """Test embederr property."""
    PIDebug('enter test_errhandling.test_gcserror_methods()')
    try:
        raise GCSError(gcserror.E10_PI_CNTR_STOP)
    except GCSError as exc:
        if gcserror.E10_PI_CNTR_STOP == exc:
            pass
        else:
            raise SystemError('GCSError "eq" operator test failed.')
    try:
        raise GCSError(gcserror.E10_PI_CNTR_STOP)
    except GCSError as exc:
        if gcserror.E10_PI_CNTR_STOP != exc:
            raise SystemError('GCSError "ne" operator test failed.')
