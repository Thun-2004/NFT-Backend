from api.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from datetime import datetime

class Collection_items(Base): 
    __tablename__ = "collection_items"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    collection_id: Mapped[int] = mapped_column(ForeignKey("collections.id"))
    nft_id: Mapped[int] = mapped_column(ForeignKey("nfts.id"))
   


