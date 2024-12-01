from api.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from datetime import datetime

class Seller(Base): 
    __tablename__ = "sellers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    bio: Mapped[str]
    profile_pic: Mapped[str | None]
    banner: Mapped[str | None]
    total_sales: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
