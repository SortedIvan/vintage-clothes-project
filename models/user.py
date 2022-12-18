from sqlalchemy import Column, Integer, String
from database.databaseConnection import base
from pydantic import BaseModel

class User(base):
    __tablename__="users"
    id=Column(String(255),primary_key=True,index=True)
    username = Column(String(255), index = True)
    user_email = Column(String(255), index = True)
    user_password = Column(String(255),index=True)