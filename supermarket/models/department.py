"""Department Model."""
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


class Department(mysql.BaseModel):
    """Department Model.

    Represents department table in supermarket.
    """

    __tablename__ = 'department'

    department_id = Column(
        Integer, primary_key=True, autoincrement=True, nullable=False)
    department_name = Column(String)

    def to_dict(self):
        """Return a dictionary of a department's properties."""
        return {
            'department_id': self.department_id,
            'department_name': self.department_name
        }
