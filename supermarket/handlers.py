"""Application Handlers.
Requests are redirected to handlers, which are responsible for getting
information from the URL and passing it down to the logic layer. The way
each layer talks to each other is through Response objects which defines the
type status of the data and the data itself.
"""
from flask import request
from oto.adaptors.flask import flaskify
from supermarket import config
from supermarket.api import app
from supermarket.logic import hello
from supermarket.logic import metadata


@app.route(config.HEALTH_CHECK, methods=['GET'])
def health():
    """Check the health of the application."""
    name = request.args.get('name', '')
    return flaskify(hello.say_hello(name))


@app.route('/api/v1/location', methods=['GET'])
def get_all_locations():
    """Get all locations.

    return Response: Flask response.
    """
    return flaskify(metadata.get_all_locations())


@app.route('/api/v1/location/<int:location_id>/department', methods=['GET'])
def get_departments_by_location(location_id):
    """Get departments by location_id.
    Args:
        location_id (int): location_id of location.

    return Response: Flask response.
    """
    return flaskify(metadata.get_departments_by_location(location_id))


@app.route('/api/v1/location/<int:location_id>/department/<int:department_id>/category', methods=['GET'])
def get_category_by_location_and_department(location_id, department_id):
    """Get categories by location_id and department_id.
    Args:
        location_id (int): location_id of location.
        department_id (int): department_id of department.

    return Response: Flask response.
    """
    return flaskify(metadata.get_category_by_location_and_department(location_id, department_id))


@app.route('/api/v1/location/<int:location_id>/department/<int:department_id>/category/<int:category_id>/subcategory', methods=['GET'])
def get_subcategory_by_location_department_category(location_id, department_id, category_id):
    """Get subcategories by location_id, department_id and category_id.
    Args:
        location_id (int): location_id of location.
        department_id (int): department_id of department.
        category_id (int): category_id of category.

    return Response: Flask response.
    """
    return flaskify(metadata.get_subcategory_by_location_department_category(location_id, department_id, category_id))


@app.route('/api/v1/location/<int:location_id>/department/<int:department_id>/category/<int:category_id>/subcategory/<int:subcategory_id>', methods=['GET'])
def get_sku(location_id, department_id, category_id, subcategory_id):
    """Get sku by location_id, department_id, category_id and subcategory_id.
    Args:
        location_id (int): location_id of location.
        department_id (int): department_id of department.
        category_id (int): category_id of category.
        subcategory_id (int): subcategory_id of subcategory.

    return Response: Flask response.
    """
    return flaskify(metadata.get_sku(location_id, department_id, category_id, subcategory_id))


@app.route('/api/v1/sku_data', methods=['GET'])
def get_sku_data():
    """Get sku by location_id, department_id, category_id and subcategory_id.

    return Response: Flask response.
    """
    location_name = request.args.get('location_name', '')
    department_name = request.args.get('department_name', '')
    category_name = request.args.get('category_name', '')
    subcategory_name = request.args.get('subcategory_name', '')
    return flaskify(metadata.get_sku_data(
        location_name=location_name, department_name=department_name,
        category_name=category_name, subcategory_name=subcategory_name))
