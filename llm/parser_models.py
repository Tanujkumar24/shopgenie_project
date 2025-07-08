from pydantic import BaseModel
from typing import List, Dict

class Product(BaseModel):
    name: str
    specs: Dict[str, str]
    ratings: Dict[str, float]
    review_summary: str

class ProductComparison(BaseModel):
    products: List[Product]
    best_product: str
    justification: str