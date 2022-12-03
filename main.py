from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import authentication
from servconf.origins import origins
from database.databaseConnection import engine, sessionLocal, base

app = FastAPI()

app.include_router(authentication.router)

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