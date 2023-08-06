#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test connection ID."""
__signature__ = 0x94dbd56c54f062fdef7854e059ace49c

from pipython import PIDebug


def test_id(gcs):
    """Test connection ID, equals 0 with PISocket."""
    PIDebug('enter test_id.test_id')
    assert 0 == gcs.connectionid
    assert 0 == gcs.GetID()
