from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from database import Base

class Address(Base):
    
    """
    Represents an address.
    Attributes:
        id (int): The unique identifier of the address.
        street (str): The street name of the address.
        city (str): The city name of the address.
        latitude (float): The latitude coordinates of the address.
        longitude (float): The longitude coordinates of the address.
    """
    
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String, index=True)
    city = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    
    
