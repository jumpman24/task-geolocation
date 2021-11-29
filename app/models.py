from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .database import SQLBase


class Location(SQLBase):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True)
    lat = Column(String(255), nullable=False)
    lon = Column(String(255), nullable=False)


class User(SQLBase):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    full_name = Column(String(255), nullable=False)
    location_id = Column(Integer, ForeignKey(Location.id), nullable=False)

    location = relationship(Location)
