"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.pigion.logic import validators


def test_pigion_reauired_with_valid_value():
    assert validators.pigion_required("value") == "value"


def test_pigion_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.pigion_required(None)
