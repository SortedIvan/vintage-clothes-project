from sqlalchemy import Column, Integer, String, Boolean, Date
from database.databaseConnection import base
from pydantic import BaseModel

#TODO: Change from string to enums or class
class Item(base):
    __tablename__="items"
    id= Column(String(255), primary_key=True,index=True)
    user_id = Column(String(255), index = True)
    item_name = Column(String(255), index = True)
    item_price = Column(String(255), index = True)
    item_category = Column(String(255), index = True)
    item_brand = Column(String(255), index = True)
    item_size = Column(Integer, index = True)
    item_color = Column(String(255), index = True)
    item_condition = Column(String(255), index = True)
    upload_date = Column(Date, index = True)
    item_hidden = Column(Boolean, index = True)
    item_favourites = Column(Integer, index = True)
    item_boosted = Column(Boolean, index = True)
    
