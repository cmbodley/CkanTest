import ckan.plugins.toolkit as tk


def pigion_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "pigion_required": pigion_required,
    }
