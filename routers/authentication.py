from fastapi import APIRouter
from database.databaseConnection import sessionLocal
from models.user import User
from data_utility.userdata import UserData
from starlette.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError



router = APIRouter() # Defines application to be a router for linking

def CheckUserEmail(useremail, session):
    try:
        user_with_same_email = session.query(User).filter(User.user_email == useremail).first()
        if user_with_same_email is not None:
            print(user_with_same_email)    
            return False
    except:
        print("Testing API")
    return True

@router.post("/api/register-user")
async def RegisterUser(userdata: UserData) -> JSONResponse:
    with sessionLocal() as session:
        if CheckUserEmail(userdata.email, session):
            user = User(
                username = userdata.dict().get("username"),
                user_email = userdata.dict().get("email"),
                user_password = userdata.dict().get("password")
            )
            #TODO: Hashing the passwords & checking for username
            session.add(user)
            session.commit()
            return JSONResponse(status_code=200, 
                content = {"message": "Sucessfully registered.", "registered":True})
        #Case where user's email already exists, we return false
        return JSONResponse(status_code=401, 
        content = {"message": "Email already exists!", "registered":False})
            
            