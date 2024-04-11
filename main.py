from fastapi import FastAPI, HTTPException, Depends, Query
from models import Address
from schema import (
    AddressCreateRequest,
    AddressCreateResponseModel,
    AddressDeleteResponseModel,
    AddressGetResponseModel,
    AddressUpdateRequestModel,
    AddressUpdateResponseModel,
)

from sqlalchemy.orm import Session
from database import get_db
from typing import List
from database import engine
from models import Base
import logging
from shapely.geometry import Point

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Logging setup
logging.basicConfig(filename="logs.log", level=logging.INFO)


@app.post(
    "/addresses/",
    response_model=AddressCreateResponseModel,
    summary="Creating an address",
)
def create_address(address: AddressCreateRequest, session: Session = Depends(get_db)):
    """
    Create a new address
    --> street: Street name
    -->city: City name
    --> latitude: Latitude coordinates
    --> longitude: Longitude coordinates

    """
    session_address = Address(**address.dict())
    session.add(session_address)
    session.commit()
    session.refresh(session_address)
    logging.info(
        f"Address created: id={session_address.id}, street={session_address.street}, city={session_address.city}, latitude={session_address.latitude}, longitude={session_address.longitude}"
    )
    return {
        "id": session_address.id,
        "msg": "Address created successfully",
        "detail": "The address has been successfully added to the address book.",
    }


@app.put(
    "/addresses/{address_id}",
    response_model=AddressUpdateResponseModel,
    summary="Updating an address",
)
def update_address(
    address_id: int,
    address: AddressUpdateRequestModel,
    session: Session = Depends(get_db),
):
    """
    Update an existing address by ID

    -->address_id: ID of the address to update
    -->street: Street name
    --> city: City name
    -->latitude: Latitude coordinates
    -->longitude: Longitude coordinates
    """
    session_address = session.query(Address).filter(Address.id == address_id).first()
    if session_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    for attr, value in address.dict().items():
        setattr(session_address, attr, value)
    session.commit()
    session.refresh(session_address)
    logging.info(f"Address id {session_address.id} updated successfully!!")
    return {
        "msg": f"Address is successfully updated",
        "detail": f"The address id {session_address.id}  has been successfully updated..",
    }


@app.delete(
    "/addresses/{address_id}",
    response_model=AddressDeleteResponseModel,
    summary="Delete an address",
)
def delete_address(address_id: int, session: Session = Depends(get_db)):
    """
    Delete an address by ID.

    -- address_id: ID of the address to delete
    """
    session_address = session.query(Address).filter(Address.id == address_id).first()
    if session_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    session.delete(session_address)
    session.commit()
    logging.info(
        f"Address deleted: id={session_address.id}, street={session_address.street}, city={session_address.city}, latitude={session_address.latitude}, longitude={session_address.longitude}"
    )
    return {
        "msg": "Address is successfully deleted",
        "detail": f"The address id {session_address.id}  has been successfully deleted from the address book.",
    }


@app.get("/addresses/", response_model=List[AddressGetResponseModel])
def get_addresses_within_distance(
    latitude: float = Query(..., description="latitude of the point"),
    longitude: float = Query(..., description="longitude of the point"),
    distance: float = Query(..., description="distance in kilometers"),
    session: Session = Depends(get_db),
):

    point = Point(longitude, latitude)
    addresses = session.query(Address).all()

    # Calculate distance between each address and the given point
    addresses = session.query(Address).all()
    point = Point(longitude, latitude)
    addresses_within_distance = [
        address
        for address in addresses
        if Point(address.longitude, address.latitude).distance(point) <= distance
    ]
    return addresses_within_distance
