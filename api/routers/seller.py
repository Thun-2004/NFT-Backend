from fastapi import APIRouter, Depends, Request, Response, UploadFile, status

router = APIRouter(
    prefix="/customers",
    tags=["customer"],
)

@router.get("/hello")
async def hello():
    return {"message": "Hello World"}