from fastapi.responses import JSONResponse
from api.configuration import Configuration
from api.errors import ConflictingError
from api.errors.authentication import AuthenticationError
from api.schemas.authentication import AuthenticationResponse
from api.state import State
from api.models.seller import Seller
from api.schemas.seller import (
    SellerBase
)


import hashlib
import datetime
import logging

async def register_seller(
    payload: SellerBase,
    state: State,
    configuration: Configuration,
) -> AuthenticationResponse:
    """Create a new merchant in the database."""
    # Check if a merchant with the same username or email already exists
    existing_seller = (
        state.session.query(Seller)
        .filter(
            (Seller.user_id == payload.user_id)
        )
        .first()
    )

    if existing_seller:
        return JSONResponse(
            content={"message": "merchant already exists"},
            status_code=409,
        )

    new_seller = Seller(
        user_id=payload.user_id,
        bio=payload.bio,
        profile_pic=None,
        banner=None,
        total_sales=0,
    )

    state.session.add(new_seller)
    state.session.commit()

    state.session.refresh(new_seller)

    return JSONResponse(
        content={"id": new_seller.id},
        status_code=201,
    )

   
# async def get_merchant(state: State, merchant_id: int) -> Merchant | None:
#     """Get a merchant by their ID."""

#     try:
#         return (
#             state.session.query(Merchant)
#             .filter(Merchant.id == merchant_id)
#             .first()
#         )
#     catch(e):
#         loggin.error(e)


async def get_seller_by_id(seller_id: int, state: State) -> Seller | None:
    """Get a merchant by their ID."""
    try:
        return (
            state.session.query(Seller)
            .filter(Seller.id == seller_id)
            .first()
        )
    except Exception as e:  # Corrected syntax
        logging.error(f"Error fetching merchant with ID {seller_id}: {e}")
        return None  # Return None explicitly in case of an error



