import pydantic


class Product(pydantic.BaseModel):
    id: int
    name: str
    thumbnail_url: str
    description: str
    short_description: str
    price: int
