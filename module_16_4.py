from fastapi import FastAPI, HTTPException, Path
from typing import Annotated

from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
        id:int
        username:str
        age:int

users = []

@app.get("/users")
async def get_users():
    return users

@app.post("/users/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, title="Enter username",
                                                description="The USERNAME must be a length  >=5 and <=20",
                                                example="UrbanUser")],
                      age: Annotated[int, Path(ge=18, le=20, title="Enter age",
                                               description="The AGE must be a integer >=18 and <=20 ",
                                               example=20)]):
   if len(users) > 0:
       id = len(users)+1
   else:
       id = 1
   item = User(id=id, username=username,  age=age)
   users.append(item)
   return item

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[str, Path(regex='^[1-9]', title="Enter user_id",
                                                   description="user_id",
                                                   example="1")],
                      username: Annotated[str, Path(min_length=5, max_length=20, title="Enter username",
                                                    description="The USERNAME must be a length  >=5 and <=20",
                                                    example="UrbanUser")],
                      age: Annotated[int, Path(ge=18, le=20, title="Enter age",
                                               description="The AGE must be a integer >=18 and <=30 ",
                                               example=24)]):
    for key in users:
        if key == user_id:
            users[str(key)] = f"Имя: {username}, возраст: {age}"
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return {"message": f"The user {user_id} is updated"}
