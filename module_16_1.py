from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


# Определение базового маршрута
@app.get("/")
async def get_main_page():
    return {"Главная страница"}


@app.get("/user/admin")
async def get_admin_page():
    return {"Вы вошли как администратор"}


# "/user/{user_id}". По нему должно выводиться сообщение "Вы вошли как пользователь № <user_id>"
@app.get("/user/{user_id}")
async def get_user_number(user_id: int):
    return {f"Вы вошли как пользователь №{user_id}"}


# Информация о пользователе. Имя: <username>, Возраст: <age>
@app.get("/user/{name}/age/{age}")
async def Get_User_Info(name: str, age: int):
    return {f"Информация о пользователе. Имя: {name}, Возраст: {age}"}
