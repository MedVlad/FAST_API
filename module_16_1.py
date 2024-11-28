from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


# Определение базового маршрута
@app.get("/")
async def Get_Main_Page():
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def Get_admin_Page()-> dict:
    return {"message": "Вы вошли как администратор"}


# "/user/{user_id}". По нему должно выводиться сообщение "Вы вошли как пользователь № <user_id>"
@app.get("/user/{user_id}")
async def Get_User_Number(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь №{user_id}"}


# Информация о пользователе. Имя: <username>, Возраст: <age>
@app.get("/user/{name}/age/{age}")
async def Get_User_Info(name: str, age: int)-> dict:
    return {"message": f"Информация о пользователе. Имя: {name}, Возраст: {age}"}
