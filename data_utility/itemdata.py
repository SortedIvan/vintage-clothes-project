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

class ItemObject(object):
  def __init__(self, user_id, item_name,item_price,item_category,item_brand,
  item_size,item_color,item_condition,upload_date,
  item_hidden,item_favourites,item_boosted):
    self.user_id = user_id
    self.item_name = item_name
    self.item_price = item_price
    self.item_category = item_category
    self.item_brand = item_brand
    self.item_size = item_size
    self.item_color = item_color
    self.item_condition = item_condition
    self.upload_date = upload_date
    self.item_hidden = item_hidden
    self.item_favourites = item_favourites
    self.item_boosted = item_boosted