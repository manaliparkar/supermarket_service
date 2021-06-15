"""Logic for Locations."""

from oto import response
from supermarket.models import location as location_model
from supermarket.models import sku as sku_model


def get_all_locations():
    """Return locations information.

    Returns:
        response.Response: location information
    """
    location_response = location_model.get_all_locations()

    return location_response

9
def get_departments_by_location(location_id):
    """Get departments by location_id.
    Args:
        location_id (int): location_id of location.

    Returns:
        response.Response: departments information.
    """
    department_response = sku_model.get_departments_by_location(location_id)

    return department_response


def get_category_by_location_and_department(location_id, department_id):
    """Get categories by location_id and department_id.
    Args:
        location_id (int): location_id of location.
        department_id (int): department_id of department.

    Returns:
        response.Response: categories information.
    """
    category_response = sku_model.get_category_by_location_and_department(location_id, department_id)

    return category_response


def get_subcategory_by_location_department_category(location_id, department_id, category_id):
    """Get subcategories by location_id, department_id and category_id.
    Args:
        location_id (int): location_id of location.
        department_id (int): department_id of department.
        category_id (int): category_id of category.

    Returns:
        response.Response: subcategories information.
    """
    subcategory_response = sku_model.get_subcategory_by_location_department_category(location_id, department_id, category_id)

    return subcategory_response


def get_sku(location_id, department_id, category_id, subcategory_id):
    """Get sku data by location_id, department_id, category_id and subcategory_id.
    Args:
        location_id (int): location_id of location.
        department_id (int): department_id of department.
        category_id (int): category_id of category.
        subcategory_id (int): subcategory_id of subcategory.

    Returns:
        response.Response: sku information.
    """
    sku_response = sku_model.get_sku(location_id, department_id, category_id, subcategory_id)

    return sku_response


def get_sku_data(location_name, department_name, category_name, subcategory_name):
    """Get sku data by location_name, department_name, category_name and subcategory_name.
    Args:
        location_name (string): name of location.
        department_name (string): name of department.
        category_name (string): name of category.
        subcategory_name (string): name of subcategory.

    Returns:
        response.Response: sku information.
    """
    sku_data_response = sku_model.get_sku_data(location_name, department_name, category_name, subcategory_name)

    return sku_data_response
