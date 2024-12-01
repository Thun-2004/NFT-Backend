from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class NFTBase(BaseModel):
    name: str
    token_uri: str
    price: float
    img: str

class NFTCreate(NFTBase):
    creator_id: int
    token_id: int
    creator_id: int
    current_owner_id: int
    status: str
    created_at: datetime

class NFTUpdate(BaseModel):
    id: int
    name: Optional[str]
    price: Optional[float]

class NFTResponse(NFTBase):
    id: int
    status: str
