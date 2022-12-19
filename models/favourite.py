from sqlalchemy import Column, String
from database.databaseConnection import base

#TODO: Change from string to enums or class
class Favourite(base):
    __tablename__="favourites"
    user_id = Column(String(255), primary_key=True,index=True)
    item_id = Column(String(255), index = True)