from fastapi import APIRouter

router = APIRouter(prefix="/v1/products", tags=["products"])


@router.get("")
async def get_products():
    return {"message": "Products fetched successfully"}
