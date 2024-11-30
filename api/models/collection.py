from api.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from datetime import datetime

class Collections(Base): 
    __tablename__ = "collections"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    creator_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    description: Mapped[str]
   


