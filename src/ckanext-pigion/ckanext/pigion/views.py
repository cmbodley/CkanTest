from flask import Blueprint


pigion = Blueprint(
    "pigion", __name__)


def page():
    return "Hello, pigion!"


pigion.add_url_rule(
    "/pigion/page", view_func=page)


def get_blueprints():
    return [pigion]
