from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str
    wallet_address: str
    

class UserRegister(UserBase):
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class User(UserBase):
    """The schema for public customer data."""
    id: int
    model_config = ConfigDict(from_attributes=True)