from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


# Определение базового маршрута
@app.get("/")
async def get_main_page():
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def get_admin_page() -> dict:
    return {"message": "Вы вошли как администратор"}


# "/user/{user_id}". По нему должно выводиться сообщение "Вы вошли как пользователь № <user_id>"
@app.get("/user/{user_id}")
async def get_user_number(user_id: Annotated[
    int, Path(ge=1, le=100, title="User ID", description="The ID must be a positive integer", example=1)]) -> dict:
    return {"message": f"Вы вошли как пользователь №{user_id}"}


# Информация о пользователе. Имя: <username>, Возраст: <age>
@app.get("/user/{username}/{age}")
async def get_user_info(username: Annotated[str, Path(min_length=5, max_length=20, title="Enter username",
                                                      description="The USERNAME must be a length  >=5 and <=20",
                                                      example="UrbanUser")],
                        age: Annotated[int, Path(ge=18, le=20, title="Enter age",
                                                 description="The AGE must be a integer >=18 and <=20 ",
                                                 example=24)]) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
