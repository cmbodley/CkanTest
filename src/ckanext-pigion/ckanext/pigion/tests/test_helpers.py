"""Tests for helpers.py."""

import ckanext.pigion.helpers as helpers


def test_pigion_hello():
    assert helpers.pigion_hello() == "Hello, pigion!"
