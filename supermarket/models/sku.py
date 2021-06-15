"""Sku Model."""
from oto import response
from sqlalchemy import Column
from sqlalchemy import exc
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import and_
from sqlalchemy.orm import relationship
from supermarket.models.location import Location
from supermarket.models.department import Department
from supermarket.models.category import Category
from supermarket.models.subcategory import Subcategory

from supermarket.connectors import mysql


class Sku(mysql.BaseModel):
    """Sku Model.

    Represents department table in supermarket.
    """

    __tablename__ = 'sku'

    sku_id = Column(
        Integer, primary_key=True, autoincrement=True, nullable=False)
    sku_name = Column(String)
    location_id = Column(
        Integer, ForeignKey('location.location_id'), nullable=False)
    department_id = Column(
        Integer, ForeignKey('department.department_id'), nullable=False)
    category_id = Column(
        Integer, ForeignKey('category.category_id'), nullable=False)
    subcategory_id = Column(
        Integer, ForeignKey('subcategory.subcategory_id'), nullable=False)
    location = relationship(Location)
    department = relationship(Department)
    category = relationship(Category)
    subcategory = relationship(Subcategory)


    def to_dict(self):
        """Return a dictionary of a sku's properties."""
        return {
            'sku_id': self.sku_id,
            'sku': self.sku_name,
            'location': self.location.location_name,
            'department': self.department.department_name,
            'category': self.category.category_name,
            'subcategory': self.subcategory.subcategory_name
        }


def get_departments_by_location(location_id):
    """Get all department information by location.
    Args:
        location_id (int): location_id of location.

    Returns:
        response.Response: containing list of departments.
    """
    with mysql.db_session(read_only=True) as session:
        department_list = []
        for department_name in session.query(Department.department_name).join(Sku).filter(
                Sku.location_id == location_id).distinct().all():
            department_list.append(department_name[0])
        if not department_list:
            return response.create_not_found_response(message='No data found.')

        return response.Response(message=department_list)


def get_category_by_location_and_department(location_id, department_id):
    """Get all department information.
    Args:
        location_id (int): location_id of location.
        department_id (int): department_id of department.

    Returns:
        response.Response: containing list of categories.
    """
    with mysql.db_session(read_only=True) as session:
        category_list = []
        for category_name in session.query(Category.category_name).join(Sku).filter(
                Sku.location_id == location_id, Sku.department_id == department_id).distinct().all():
            category_list.append(category_name[0])
        if not category_list:
            return response.create_not_found_response(message='No data found.')

        return response.Response(message=category_list)


def get_subcategory_by_location_department_category(location_id, department_id, category_id):
    """Get all subcategory information.
    Args:
        location_id (int): location_id of location.
        department_id (int): department_id of department.
        category_id (int): category_id of category.

    Returns:
        response.Response: containing list of subcategories.
    """
    with mysql.db_session(read_only=True) as session:
        subcategory_list = []
        for subcategory_name in session.query(Subcategory.subcategory_name).join(Sku).filter(
                Sku.location_id == location_id, Sku.department_id == department_id,
                Sku.category_id == category_id).distinct().all():
            subcategory_list.append(subcategory_name[0])
        if not subcategory_list:
            return response.create_not_found_response(message='No data found.')

        return response.Response(message=subcategory_list)


def get_sku(location_id, department_id, category_id, subcategory_id):
    """Get all sku information.
    Args:
        location_id (int): location_id of location.
        department_id (int): department_id of department.
        category_id (int): category_id of category.
        subcategory_id (int): subcategory_id of subcategory.

    Returns:
        response.Response: containing list of sku data with specified filters.
    """
    with mysql.db_session(read_only=True) as session:
        sku_data = session.query(Sku).filter(
                Sku.location_id == location_id, Sku.department_id == department_id,
                Sku.category_id == category_id, Sku.subcategory_id == subcategory_id).all()

        if not sku_data:
            return response.create_not_found_response(message='No data found.')
        sku_list = [sku.to_dict() for sku in sku_data]

        return response.Response(message=sku_list)


def get_sku_data(location_name, department_name, category_name, subcategory_name):
    """Get all sku information.
    Args:
        location_name (string): name of location.
        department_name (string): name of department.
        category_name (string): name of category.
        subcategory_name (string): name of subcategory.

    Returns:
        response.Response: containing list of sku data with specified filters.
    """
    with mysql.db_session(read_only=True) as session:
        filters = []
        joins = []
        if location_name:
            filters.append(Location.location_name == location_name)
            joins.append(Location)
        if department_name:
            filters.append(Department.department_name == department_name)
            joins.append(Department)
        if category_name:
            filters.append(Category.category_name == category_name)
            joins.append(Category)
        if subcategory_name:
            filters.append(Subcategory.subcategory_name == subcategory_name)
            joins.append(Subcategory)
        sku_data = session.query(Sku).join(*joins).filter(*filters).all()
        if not sku_data:
            return response.create_not_found_response(message='No data found.')

        sku_list = [sku.to_dict() for sku in sku_data]

        return response.Response(message=sku_list)
