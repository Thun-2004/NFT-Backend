from api.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from datetime import datetime

class Nft(Base): 
    __tablename__ = "nfts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    token_id: Mapped[int]
    name : Mapped[str]
    contract_address: Mapped[str]
    token_uri: Mapped[str]
    creator_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    current_owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    price: Mapped[float]
    img: Mapped[str]
    status: Mapped[str]  # e.g., "minted", "listed", "sold"
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)


