import ckan.plugins.toolkit as tk
import ckanext.pigion.logic.schema as schema


@tk.side_effect_free
def pigion_get_sum(context, data_dict):
    tk.check_access(
        "pigion_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.pigion_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'pigion_get_sum': pigion_get_sum,
    }
