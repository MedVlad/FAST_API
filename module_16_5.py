from fastapi import FastAPI, Request, HTTPException, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from typing import Annotated, List
app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
# Настраиваем Jinja2 для загрузки шаблонов из папки templates
templates = Jinja2Templates(directory="templates")

class User(BaseModel):
    id: int
    username: str
    age: int

users = []



@app.get("/", response_class=HTMLResponse)
async def get_main_page(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_user(request:Request, user_id: Annotated[int, Path(ge=1)]):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}", response_class=HTMLResponse)
async def delete_user(request:Request, user_id: Annotated[int, Path(ge=1)]):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User was not found")

@app.post("/user/{username}/{age}", response_class=HTMLResponse)
async def create_user(
    request: Request, username: Annotated[str, Path(min_length=3, max_length=100)],
    age: Annotated[int, Path()]):
    new_id = max(user.id for user in users) + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.put("/user/{user_id}/{username}/{age}", response_class=HTMLResponse)
async def update_user(request:Request, user_id: Annotated[int, Path(ge=1)],
                   username: Annotated[str, Path(min_length=3, max_length=100)],
                   age: Annotated[int, Path()]):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User was not found")