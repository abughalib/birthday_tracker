from server.models.api_model import UserInfoAPI
from server import middleware
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def index():
    return { "intro": "Hello" }

@app.get("/get_birthday_today")
async def get_birthday_today():
    return {"birthdays": middleware.find_birthday_today()}

@app.get("/set_birthday")
async def set_birthday(user_info: UserInfoAPI):

    if middleware.insert_birthday(user_info):
        return {
                "Status": "Success",
                "Inserted": user_info
                }

    return {"status": "Cannot insert data"}
