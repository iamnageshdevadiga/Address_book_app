from pydantic import BaseModel
from typing import Optional

class AddressCreateRequest(BaseModel):
    """
    --Address Create Create Request MOdel
    """
    street: str
    city: str
    latitude: float
    longitude: float
    
class BaseResponseModel(BaseModel):
    """
    --SSBase Response model
    """
    msg:str
    detail:str
    
class AddressCreateResponseModel(BaseResponseModel):
    """
    --Address Create Response MOdel
    """
    id:int
    
class AddressDeleteResponseModel(BaseResponseModel):
    """
    --Address Delete Response MOdel
    """
    ...

class AddressGetResponseModel(BaseModel):
    """
    --Address Get Response MOdel
    """
    id:int
    street: str
    city: str
    latitude: float
    longitude: float
    
class AddressUpdateRequestModel(BaseModel):
    """
    --Address Update Request MOdel
    """
    street: Optional[str] = None
    city: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    
class AddressUpdateResponseModel(BaseResponseModel):
    """
    --Address Update Response MOdel
    """
    ...