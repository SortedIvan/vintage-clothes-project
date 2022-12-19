from fastapi import APIRouter, Form, Depends
from database.databaseConnection import sessionLocal
from models.item import Item
from starlette.responses import JSONResponse
from django.http import JsonResponse
from data_utility.itemdata import ItemData, ItemObject, ItemObj
import datetime
import uuid
from fastapi_pagination import Page, add_pagination, paginate, Params
import json




router = APIRouter()


def obj_dict(obj):
    if isinstance(obj, datetime.date):
        return dict(year=obj.year, month=obj.month, day=obj.day)
    else:
        return obj.__dict__

@router.post("/api/create-new-listing")
async def CreateNewItem(itemData: ItemData) -> JsonResponse:
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

@router.get("/api/get-all-user-items", response_model=Page[ItemObj])
async def GetAllUserItems(user_id, params: Params = Depends()):
    with sessionLocal() as session:
        items = session.query(Item).filter(Item.user_id == user_id).all()

        all_items_json = []
        for i in range(len(items)):
            item_data = {
                "user_id": items[i].user_id,
                "item_name": items[i].item_name,
                "item_price": items[i].item_price,
                "item_category": items[i].item_category,
                "item_brand": items[i].item_brand,
                "item_size":items[i].item_size,
                "item_color": items[i].item_color,
                "item_condition":items[i].item_condition,
                "upload_date": items[i].upload_date,
                "item_hidden": items[i].item_hidden,
                "item_favourites": items[i].item_favourites,
                "item_boosted":items[i].item_boosted
            }
            
            item_obj = ItemObj(**item_data)
            all_items_json.append(item_obj)
    return paginate(all_items_json, params)


