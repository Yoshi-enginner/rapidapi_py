from fastapi import FastAPI
import json
from  schema import Items,Item

app = FastAPI()

test = open("C:\\Users\\tokyo\\AppData\\Local\\TEST2022\\sample.json",'r')
sample_data = json.load(test)

@app.get("/items",response_model=Items)
async def get_messages():

    return sample_data

@app.post("/items",response_model=Item)
async def create(item:Item):

    sample_data["data"].append({"Message":item.Message})

    return {"Message":item.Message}


@app.patch("/items/{id}",response_model=Item)
async def update(id:int, item: Item):

    sample_data["data"][id] = {"Message": item.Message}

    return sample_data["data"][id]
