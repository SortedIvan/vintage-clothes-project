from fastapi import APIRouter, Form, Depends
from database.databaseConnection import sessionLocal
from models.item import Item
from starlette.responses import JSONResponse
from django.http import JsonResponse
from data_utility.itemdata import ItemData, ItemObj
from models.favourite import Favourite
import datetime
import uuid
from fastapi_pagination import Page, paginate, Params

router = APIRouter()

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

#Query all items where user_id is present
#Paginate them, where max is 100 items per page and minimum 1 page
@router.get("/api/get-all-user-items", response_model=Page[ItemObj])
async def GetAllUserItems(user_id, params: Params = Depends()):
    with sessionLocal() as session:
        items = session.query(Item).filter(Item.user_id == user_id).all()
        if items != []:
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
        else:
            return JSONResponse(status_code=200, content = {"message":"No items to show!"})


# Delete item based on the provided item_id
# NULL check if item is none -> not deleted
@router.delete("/api/delete-item/{item_id}")
async def DeleteItem(item_id):
    with sessionLocal() as session:
        item = session.query(Item).filter(Item.id == item_id).first()
        if item != None:
            session.delete(item)
            session.commit()
            return JSONResponse(status_code=200, content = {"message":"Item with id {item_id} has been deleted successfully!"})
        return JSONResponse(status_code=406, content = {"message":"Item not deleted!"})

@router.put("/api/favourite-item")
async def FavouriteItem(item_id, user_id):
    with sessionLocal() as session:
        item = session.query(Item).filter(Item.id == item_id).first()
        if item != None:
            already_favourite = session.query(Favourite).filter(Favourite.item_id == item_id).filter(Favourite.user_id == user_id).first()
            if already_favourite is not None:
                print(already_favourite)
                return JSONResponse(status_code=200, content = {"message": "Item has already been favourited!"})

            item.item_favourites += 1
            favourite = Favourite(user_id = user_id, item_id = item_id)
            session.add(favourite)
            session.commit()

            return JSONResponse(status_code=200, content = {"message": "Item has been favourited successfuly"})
        return JSONResponse(status_code=406, content= {"message": "No such item!"})

@router.put("/api/unfavourite-item")
async def FavouriteItem(item_id, user_id):
    with sessionLocal() as session:
        item = session.query(Item).filter(Item.id == item_id).first()
        if item != None:
            already_favourite = session.query(Favourite).filter(Favourite.item_id == item_id).filter(Favourite.user_id == user_id).first()
            item.item_favourites -= 1
            session.delete(already_favourite)
            session.commit()
            return JSONResponse(status_code=200, content = {"message": "Item has been unfavourited successfuly"})
        return JSONResponse(status_code=406, content= {"message": "No such item!"})
            

