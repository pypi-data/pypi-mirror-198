#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test getter commands returning a dict of int/str/any with this signature: CMD opt opt."""

# Redefining name 'cmd' from outer scope pylint: disable=W0621
__signature__ = 0x6e47cdcb300a961f92eb8785165355cf

from pipython import PIDebug
from collections import OrderedDict
import pytest
from test.tools import checksvr, cmdstr, GCSRaise
from pipython import gcserror

CMDS = [
    'qRTD',
]


@pytest.fixture(scope="module", params=CMDS, autouse=True)
def cmd(request):
    """Return items of "CMDS" for dependency injection."""
    return request.param


def test_get_noargs(gcs, cmd):
    """No arguments."""
    PIDebug('enter test_get_3arg_opt_opt_[opt]__gcs.test_get_noargs(%s)', cmd)
    gcs.svr.queue(cmdstr(cmd, '1 1 1 2 3'), '1 1 1 = 1 \n1 1 2 = 2 \n1 1 3 = 3\n')
    assert OrderedDict([((1, 1), OrderedDict([(1, '1'), (2, '2'), (3, '3')]))]) == getattr(gcs, cmd)(1, 1, [1, 2, 3])
    checksvr(gcs)


import __main__ as main
if __name__ == '__main__':
    print(main.__file__)
    pytest.main(["-x", main.__file__])
