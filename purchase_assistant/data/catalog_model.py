from typing import Annotated
from pydantic import BaseModel, Field


class Product(BaseModel):
    PRODUCT_ID: int
    Name: str
    Description: str
    Price: Annotated[int, Field(gt=1)]
    Stock_availabiility: Annotated[int, Field(gt=0)]
