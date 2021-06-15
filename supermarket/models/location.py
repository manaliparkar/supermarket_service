"""Location Model."""
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


class Location(mysql.BaseModel):
    """Location Model.

    Represents location table in supermarket.
    """

    __tablename__ = 'location'

    location_id = Column(
        Integer, primary_key=True, autoincrement=True, nullable=False)
    location_name = Column(String)

    def to_dict(self):
        """Return a dictionary of a location's properties."""
        return {
            'location_id': self.location_id,
            'location_name': self.location_name
        }


@mysql.wrap_db_errors
def get_all_locations():
    """Get all location information.

    Returns:
        response.Response: containing dict of locations.
    """
    with mysql.db_session(read_only=True) as session:
        locations = session.query(Location)

        if not locations:
            return response.create_not_found_response(message='No data found.')
        locations_list = [location.to_dict() for location in locations.all()]

        return response.Response(message=locations_list)

