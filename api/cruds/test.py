# from api.models import Base
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from sqlalchemy import ForeignKey, PrimaryKeyConstraint
# from datetime import datetime

# class Seller(Base): 
#     __tablename__ = "sellers"

#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#     bio: Mapped[str]
#     profile_pic: Mapped[str | None]
#     banner: Mapped[str | None]
#     total_sales: Mapped[int] 
#     created_at: Mapped[datetime] = mapped_column(default=datetime.now)


# from api.models import Base
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from sqlalchemy import ForeignKey, PrimaryKeyConstraint
# from datetime import datetime

# class Nft(Base): 
#     __tablename__ = "nfts"

#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     token_id: Mapped[int]
#     name : Mapped[str]
#     contract_address: Mapped[str]
#     token_uri: Mapped[str]
#     creator_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#     current_owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#     price: Mapped[float]
#     img: Mapped[str]
#     status: Mapped[str]  # e.g., "minted", "listed", "sold"
#     created_at: Mapped[datetime] = mapped_column(default=datetime.now)

# from api.models import Base
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from sqlalchemy import ForeignKey, PrimaryKeyConstraint
# from datetime import datetime

# class Listings(Base): 
#     __tablename__ = "listings"

#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     nft_id: Mapped[int] = mapped_column(ForeignKey("nfts.id"))
#     token_uri: Mapped[str]
#     status: Mapped[str] = mapped_column(default="unsold")
#     created_at: Mapped[datetime] = mapped_column(default=datetime.now)


# from api.models import Base
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from sqlalchemy import ForeignKey, PrimaryKeyConstraint
# from datetime import datetime

# class Collections(Base): 
#     __tablename__ = "collections"
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     name: Mapped[str]
#     creator_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#     description: Mapped[str]
   

# from api.models import Base
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from sqlalchemy import ForeignKey, PrimaryKeyConstraint
# from datetime import datetime

# class Collection_items(Base): 
#     __tablename__ = "collection_items"

#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     collection_id: Mapped[int] = mapped_column(ForeignKey("collections.id"))
#     nft_id: Mapped[int] = mapped_column(ForeignKey("nfts.id"))
   

