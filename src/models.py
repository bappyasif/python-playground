from pydantic import BaseModel, Field
from typing import Optional

# with pydantic model we are able to validate our data and not have to do it manually
class Product(BaseModel):
    id: int
    name: str
    # description: str
    # price: float
    # quantity: int
    description: str = Field(min_length=4, description="Description must be at least 4 characters long")
    price: float = Field(gt=0, description="Price must be greater than 0")
    quantity: int = Field(gt=0, description="Quantity must be greater than 0")

class PatchProduct(BaseModel):
    id: int
    name: Optional[str] = None
    description: Optional[str] = Field(None, min_length=4, description="Description must be at least 4 characters long")
    price: Optional[float] = Field(None, gt=0, description="Price must be greater than 0")
    quantity: Optional[int] = Field(None, gt=0, description="Quantity must be greater than 0")


# crude model for product without pydantic model where we have to do validation manually
class ProductCrude:
    id: int
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, id: int, name: str, description: str, price: float, quantity: int):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity