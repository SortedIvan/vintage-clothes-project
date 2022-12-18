from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from routers import authentication, item_manager
from servconf.origins import origins
from database.databaseConnection import engine, sessionLocal, base
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()

app.include_router(authentication.router)
app.include_router(item_manager.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Main API for the application, shown at origin page
@app.get("/")
async def root():
  return {"message": "Welcome to VintageClothing!"}

base.metadata.create_all(bind=engine)