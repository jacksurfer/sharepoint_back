from timeit import default_timer as timer

from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .sharepoint import add_equipment_request

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    email: str
    equip_type: str
    equip: str
    count: int
    ship: str


@app.get('/')
async def status():
    return {'status': 'ok'}


@app.post("/requestEquipment")
async def add_item_endpoint(item: Item, background_tasks: BackgroundTasks):
    start = timer()
    background_tasks.add_task(add_equipment_request, item.email, item.equip_type, item.equip, item.count, item.ship)
    end = timer()
    return {'data': item, 'time': end - start}
