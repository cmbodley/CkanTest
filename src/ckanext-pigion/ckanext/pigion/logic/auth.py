import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def pigion_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "pigion_get_sum": pigion_get_sum,
    }
