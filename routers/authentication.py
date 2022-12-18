from fastapi import APIRouter, Form, Depends
from database.databaseConnection import sessionLocal
from models.user import User
from data_utility.userdata import UserData, UserDataLogin
from starlette.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter() # Defines application to be a router for linking

# #TESTING ENDPOINT
# @router.post("/api/main")
# async def profile_pic(token):

# oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")
# @router.post("/token")
# async def Login(form_data: OAuth2PasswordRequestForm = Depends()):
#     print(form_data)
#     return {"access_token":'', "token_type": "bearer"}


def CheckUserEmail(useremail, session):
    try:
        user_with_same_email = session.query(User).filter(User.user_email == useremail).first()
        if user_with_same_email is not None:
            print(user_with_same_email)    
            return False
    except:
        print("Testing API")
    return True


#TODO: Salt password on register and give the user a token response
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


@router.post("/api/login-user")
async def RegisterUser(userdata: UserDataLogin) -> JSONResponse:
    with sessionLocal() as session:
        user = session.query(User).filter(User.user_email == userdata.email).first()
        if user.user_password == userdata.password:
            #TODO: De-salt password 
            return JSONResponse(status_code=200, 
                content = {"message": "Succesful login.", "logged_in":True})
        return JSONResponse(status_code=401, 
            content = {"message": "Unsuccesful login.", "logged_in":False})
