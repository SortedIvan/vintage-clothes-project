from fastapi import APIRouter, Form, Depends
from database.databaseConnection import sessionLocal
from models.item import Item
from starlette.responses import JSONResponse
from data_utility.itemdata import ItemData
import datetime
import uuid
import json

router = APIRouter()

@router.post("/api/create-new-listing")
async def CreateNewItem(itemData: ItemData) -> JSONResponse:
    date = datetime.datetime.now()
    with sessionLocal() as session:
        item = Item (
            id = str(uuid.uuid4()),
            user_id = itemData.dict().get("user_id"),
            item_name = itemData.dict().get("item_name"),
            item_price = itemData.dict().get("item_price"),
            item_category = itemData.dict().get("item_category"),
            item_brand = itemData.dict().get("item_brand"),
            item_color = itemData.dict().get("item_color"),
            item_size = itemData.dict().get("item_size"),
            item_condition = itemData.dict().get("item_condition"),
            upload_date = date.strftime("%d/%m/%Y"),
            item_hidden = False,
            item_boosted = itemData.dict().get("item_boosted"),
            item_favourites = 0
        )
        session.add(item)
        session.commit()

    return JSONResponse(status_code=200, 
        content = {"message": "Listing created successfuly!", "item_created": True, "user_id": itemData.dict().get("user_id"), "item_name": itemData.dict().get("item_name"), 
        "item_price":itemData.dict().get("item_price"), "item_category": itemData.dict().get("item_category"), 
        "item_brand":  itemData.dict().get("item_brand"), "item_color": itemData.dict().get("item_color"),
        "item_size": itemData.dict().get("item_size"), "item_condition": itemData.dict().get("item_condition"), "upload_date": date.strftime("%d/%m/%Y"),
        "item_hidden": False})




