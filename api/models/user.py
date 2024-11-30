from api.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from datetime import datetime

class User(Base): 
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    wallet_address: Mapped[str]
    username: Mapped[str]
    email: Mapped[str]
    hashed_password: Mapped[str]
    salt: Mapped[str]
    bio: Mapped[str] 
    profile_pic: Mapped[str | None]
    banner: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
