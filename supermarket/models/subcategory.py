"""Subcategory Model."""
from oto import response
from sqlalchemy import asc
from sqlalchemy import BigInteger
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import desc
from sqlalchemy import Enum
from sqlalchemy import exc
from sqlalchemy import Integer
from sqlalchemy import String

from supermarket.connectors import mysql
# from supermarket.connectors.sentry import sentry_client
# from supermarket.constants import error


class Subcategory(mysql.BaseModel):
    """Subcategory Model.

    Represents department table in supermarket.
    """

    __tablename__ = 'subcategory'

    subcategory_id = Column(
        Integer, primary_key=True, autoincrement=True, nullable=False)
    subcategory_name = Column(String)

    def to_dict(self):
        """Return a dictionary of a subcategory's properties."""
        return {
            'subcategory_id': self.subcategory_id,
            'subcategory_name': self.subcategory_name
        }
