from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer

from api.configuration import Configuration
from api.cruds.seller import (
    register_seller,
    get_seller_by_id
)
from api.dependencies.id import get_customer_id


from api.dependencies.configuration import get_configuration
from api.dependencies.state import get_state
from api.errors import NotFoundError
from api.schemas.authentication import AuthenticationResponse
from api.schemas.seller import (
    SellerBase,
    Seller
)
from api.state import State


router = APIRouter(
    prefix="/seller",
    tags=["seller"],
)


@router.post(
    "/register",
    description="""
        Registers a new user and returns a JWT token used for authentication.
    """,
)
async def register_seller_api(
    payload: SellerBase,
    state: State = Depends(get_state),
    configuration: Configuration = Depends(get_configuration),
) -> JSONResponse:
    return await register_seller(state, configuration, payload)

#get all seller 

#get seller by id
@router.get(
    "/{seller_id}",
    description="""
        Get the public information of a user by their ID.
    """,
)
async def get_seller_by_id_api(
    seller_id: int,
    state: State = Depends(get_state),
) -> Seller:
    result = await get_seller_by_id(state, seller_id)

    if not result:
        raise NotFoundError("merchant not found")

    return result


