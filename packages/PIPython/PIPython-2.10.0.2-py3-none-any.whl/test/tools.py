#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Collection of test helper functions."""

# Anomalous backslash in string pylint: disable=W1401
__signature__ = 0x806d8451d5ff9f61c29644ab41f6b866

from pipython import PIDebug


CMDS = {
    'GetPosStatus': '%s' % chr(3),
    'GetStatus': '%s' % chr(4),
    'IsMoving': '%s' % chr(5),
    'HasPosChanged': '%s' % chr(6),
    'IsControllerReady': '%s' % chr(7),
    'IsRunningMacro': '%s' % chr(8),
    'IsGeneratorRunning': '%s' % chr(9),
    'GetDynamicMoveBufferSize': '%s' % chr(11),
    'StopAll': '%s' % chr(24),
    'qIDN': '*IDN?',
    'DMOV': 'MOV!',
    'qSAI_ALL': 'SAI? ALL'
}


def cmdstr(funcname, suffix=''):
    """Return GCS command string from 'funcname' and 'suffix'.
    @param funcname : Name of function as string.
    @param suffix : String that will be appended after the command name.
    @return : Command string with trailing linefeed.
    """
    if funcname in CMDS:
        cmd = CMDS[funcname]
        if len(cmd) == 1:
            return cmd
    else:
        cmd = funcname
        if '_q' in cmd:
            cmd = cmd.replace('_q', ' ')
            cmd = '%s?' % cmd
        if '_' in cmd:
            cmd = cmd.replace('_', ' ')
        if cmd.startswith('q'):
            cmd = '%s?' % cmd[1:]
    if suffix:
        cmd += ' %s' % suffix
    return '%s\n' % cmd


class GCSRaise(object):  # Too few public methods pylint: disable=R0903
    """Context manager that asserts raising of specific GCSError(s).
    @param gcserror : GCSError or iterable of GCSErrors that is expected to be raised as integer.
    @param mustraise : If True an exception must be raised, if False an exception can be raised.
    """

    def __init__(self, gcserror, mustraise=True):
        self.__expected = gcserror if isinstance(gcserror, (list, set, tuple)) else [gcserror]
        self.__mustraise = mustraise and gcserror

    def __enter__(self):
        return self

    def __exit__(self, exctype, excvalue, _exctraceback):
        from pipython import GCSError, gcserror
        gcsmsg = 'GCSError %r' % gcserror.translate_error(excvalue)
        if exctype == GCSError:
            if excvalue in self.__expected:
                PIDebug('expected %s was raised', gcsmsg)
                return True  # do not re-raise
        if not self.__mustraise and excvalue is None:
            PIDebug('no error was raised')
            return True  # do not re-raise
        expected = ', '.join([gcserror.translate_error(errval) for errval in self.__expected])
        msg = 'expected %r but raised was %s' % (expected, gcsmsg)
        raise AssertionError(msg)


def checksvr(gcs):
    """Call a query command to sync ReplyServer and then check server for no error."""
    gcs.svr.queue('checksvr?\n', '\n')
    gcs.ReadGCSCommand('checksvr?')
    assert gcs.svr.check
