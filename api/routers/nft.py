from datetime import timedelta
from typing import List
from fastapi import APIRouter, Depends, Request, Response, UploadFile, status
from fastapi.responses import FileResponse
from fastapi.security import HTTPBearer

from api.configuration import Configuration
from api.dependencies.configuration import get_configuration
from api.dependencies.state import get_state
from api.dependencies.id import get_customer_id
from api.cruds.nft import (
    create_nft,
    get_nfts,
    update_nft,
    buy_nft, 
    upload_nft_img, 
    get_nft_img
)

from api.state import State
from api.schemas.nft import NFTCreate, NFTUpdate, NFTResponse

router = APIRouter(
    prefix="/nft",
    tags=["nft"],
)

@router.post(
    "/",
    description="""
        Create NFT
    """,
)
async def create_nft_api(
    payload: NFTCreate,
    state: State = Depends(get_state),
    customer_id: int = Depends(get_customer_id)
) -> int: 
    return await create_nft(state, payload, customer_id)


@router.get(
    "/{user_id}",
    description="""
        get NFTs from user id
    """,
)
async def get_nft_api(
    user_id: int, 
    state: State = Depends(get_state),
) -> List[NFTResponse]: 
    return await get_nfts(state, user_id)

@router.put(
    "/update_nft/{id}",
    description="""
        Update NFT
    """,
)
async def update_nft_api(
    payload: NFTUpdate,
    customer_id: int = Depends(get_customer_id),
    state: State = Depends(get_state)
) -> None: 
    return await update_nft(state, payload, customer_id)


@router.post(
    "/{seller_id}/{nft_id}",
    description="Buy an NFT and transfer ownership.",
)
async def buy_nft_api(
    nft_id: int, 
    seller_id: int,
    customer_id: int = Depends(get_customer_id), 
    state: State = Depends(get_state)
) -> None:
    return await buy_nft(state, nft_id, seller_id, customer_id)

@router.post(
    "/upload_img/{nft_id}",
    description="""
        Upload user profile pic
    """,
)
async def upload_nft_img_api(
    image: UploadFile,
    nft_id: int,
    customer_id: int = Depends(get_customer_id),
    configuration: Configuration = Depends(get_configuration),
    state: State = Depends(get_state),
) -> str:
    await upload_nft_img(configuration, image, nft_id, customer_id, state)
    return "success"


@router.get(
    "/get_img/{nft_id}",
    description="""
        Get user profile pic
    """,
    responses={
        204: {
            "description": "the customer does not have profile image",
            "content": {"application/json": {}},
        },
        200: {
            "description": "The profile image",
            "content": {
                "image/*": {},
            },
        },
    },
    response_model=None,
    response_class=Response,
)
async def get_nft_img_api(
    response: Response,
    nft_id: int,
    state: State = Depends(get_state),
) -> FileResponse | None:

    image = await get_nft_img(state, nft_id)
    match image:
        case None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return None
        case image:
            return image
    