"""Category Model."""
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


class Category(mysql.BaseModel):
    """Category Model.

    Represents category table in supermarket.
    """

    __tablename__ = 'category'

    category_id = Column(
        Integer, primary_key=True, autoincrement=True, nullable=False)
    category_name = Column(String)

    def to_dict(self):
        """Return a dictionary of a category's properties."""
        return {
            'category_id': self.category_id,
            'category_name': self.category_name
        }
