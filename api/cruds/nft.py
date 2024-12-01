
import os
from fastapi import UploadFile
from fastapi.responses import FileResponse, JSONResponse
from api.configuration import Configuration
from api.errors import NotFoundError
from api.state import State
from api.schemas.nft import NFTCreate, NFTUpdate, NFTResponse
from api.models.nft import Nft
from typing import List

async def create_nft(
    state: State, 
    payload: NFTCreate, 
    customer_id: int) -> int: 
    pass

async def get_nfts(
    state: State, 
    user_id: int) -> List[NFTResponse]: 

    nfts = (
        state.session.query(Nft)
        .filter(
            (Nft.current_owner_id == user_id)
        )
        .all()
    )
    return [NFTResponse.model_validate(nft) for nft in nfts]


async def update_nft(
    state: State,
    payload: NFTUpdate,
    customer_id: int) -> JSONResponse: 
    nft = (
        state.session.query(Nft)
        .filter(
            (Nft.id == payload.id and Nft.creator_id == customer_id)
        )
        .first()
    )

    if nft is None:
        return JSONResponse(
                status_code=404,
                content={"message": "NFT not found"},
            )
    
    nft.name = payload.name
    nft.price = payload.price

    state.session.commit()
    return JSONResponse(
                status_code=200,
                content={"message": "NFT updated successfully"},
            )
    

async def buy_nft(
    state: State, 
    nft_id: int,
    seller_id: int, 
    customer_id: int) -> None: 
    pass
    

async def upload_nft_img(
    configuration: Configuration,
    image: UploadFile,
    nft_id: int,
    customer_id: int,
    state: State,
) -> str:
    nft = (
        state.session.query(Nft)
        .filter(Nft.id == nft_id and Nft.creator_id == customer_id)
        .first()
    )

    if not nft:
        raise NotFoundError("Customer not found")

    image_dir = os.path.join(
        configuration.application_data_path,
        "nft/img",
        str(nft_id),
    )
    image_path = await configuration.upload_image(image, image_dir)
    print(image_path)
    nft.img = image_path
    state.session.commit()
    return image_path


async def get_nft_img(
    state: State, nft_id: int
) -> FileResponse | None:
    nft = (
        state.session.query(Nft)
        .filter(Nft.id == nft_id)
        .first()
    )

    if not nft:
        raise NotFoundError("NFT not found")

    if not nft.img:
        return None

    return FileResponse(nft.img)


