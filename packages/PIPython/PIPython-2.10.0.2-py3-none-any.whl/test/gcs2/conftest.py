#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Provide fixtures for GCSCommands tests."""

# Redefining name from outer scope pylint: disable=W0621
__signature__ = 0x4762878c8ba0a9300e90f74e8a7a2d7c

import logging

import pytest

from pipython.gcsmessages import GCSMessages
from pipython.pidevice.gcs2.gcs2commands import GCS2Commands
from pipython.interfaces.pisocket import PISocket
from pipython.pitools.replyserver import ReplyServer

#logging.basicConfig(level=logging.DEBUG)  # Enable logger


# Unused argument 'request' pylint: disable=W0613
@pytest.yield_fixture(scope='session', autouse=True)
def gcs(request):
    """Setup GCSCommands and ReplyServer for dependency injection."""
    with ReplyServer(host='localhost', port=50000) as replyserver:
        with PISocket(host='localhost', port=50000) as interface:
            messages = GCSMessages(interface)
            gcscommands = GCS2Commands(messages)
            gcscommands.devname = 'C-884'  # needed to check for GCS1/2
            gcscommands.errcheck = False
            gcscommands.svr = replyserver
            yield gcscommands
