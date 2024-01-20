from fastapi import FastAPI
import json
from  schema import Items

app = FastAPI()

test = open("C:\\Users\\tokyo\\AppData\\Local\\TEST2022\\sample.json",'r')
sample_data = json.load(test)

@app.get("/items",response_model=Items)
async def get_messages():

    return sample_data