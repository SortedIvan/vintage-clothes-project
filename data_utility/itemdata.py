from pydantic import BaseModel

class ItemData(BaseModel):
    user_id: str
    item_name: str
    item_price: str 
    item_category: str 
    item_brand: str
    item_color: str 
    item_condition: str 
    item_boosted: bool
    item_size: str 