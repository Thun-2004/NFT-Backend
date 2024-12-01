from pydantic import BaseModel, ConfigDict

class SellerBase(BaseModel):
    user_id: int
    total_sales: int
    bio: str
    profile_pic: str
    banner: str

    
class Seller(SellerBase):
    """The schema for public Seller data."""

    id: int
    model_config = ConfigDict(from_attributes=True)

