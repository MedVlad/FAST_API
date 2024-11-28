from fastapi import FastAPI, HTTPException, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users():
    return users


@app.post("/users/{name}/{age}")
async def create_user(name: Annotated[str, Path(min_length=5, max_length=20, title="Enter username",
                                                description="The USERNAME must be a length  >=5 and <=20",
                                                example="UrbanUser")],
                      age: Annotated[int, Path(ge=18, le=20, title="Enter age",
                                               description="The AGE must be a integer >=18 and <=20 ",
                                               example=24)]):
    new_key = max(str(int(key) + 1) for key in users) if users else 1
    users[new_key] = f"Имя: {name}, возраст: {age}"
    return {"message": f"User {new_key} is registered"}


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


@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    for key in users:
        if key == user_id:
            del users[key]
            return {"message": "пользователь удален"}
        raise HTTPException(status_code=404, detail="Пользователь не найден")
