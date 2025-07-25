from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    brand: str
    size: str
    price: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    product_id: int
    model_config = {"from_attributes": True}

# --- Price Schemas ---
class PriceBase(BaseModel):
    store_id: int
    product_id: int
    price: float
    sale_price: Optional[float] = None
    is_on_sale: Optional[bool] = False
    sale_start: Optional[datetime] = None
    sale_end: Optional[datetime] = None
    updated_at: datetime

class PriceCreate(PriceBase):
    pass

class Price(PriceBase):
    price_id: int
    model_config = {"from_attributes": True}

# --- Inventory Schemas ---
class InventoryBase(BaseModel):
    store_id: int
    product_id: int
    quantity: int
    last_restocked: Optional[datetime] = None
    updated_at: datetime

class InventoryCreate(InventoryBase):
    pass

class Inventory(InventoryBase):
    inventory_id: int
    model_config = {"from_attributes": True}
