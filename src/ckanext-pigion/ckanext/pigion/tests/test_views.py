"""Tests for views.py."""

import pytest

import ckanext.pigion.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "pigion")
@pytest.mark.usefixtures("with_plugins")
def test_pigion_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("pigion.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, pigion!"
