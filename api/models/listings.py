from api.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from datetime import datetime

class Listings(Base): 
    __tablename__ = "listings"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nft_id: Mapped[int] = mapped_column(ForeignKey("nfts.id"))
    token_uri: Mapped[str]
    status: Mapped[str] = mapped_column(default="unsold")
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)


