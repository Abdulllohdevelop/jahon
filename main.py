from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()
class userm(BaseModel):
    ismi:str
    yoshi:int
class usern(BaseModel):
    id:int
    ismi:str
    yoshi:int
users = [{
    "ismi":"Abdulloh",
    "yoshi":12
}]
@app.get("/a")
def a():
    return users
@app.post("/a/add")
def a(user:userm):
    users.append(user.dict())
    return f"{user.ismi}malum"
@app.put("/a/update")
def updatea(user_id:int, updatea:usern):
    for user in users:
        if user["id"]  ==user_id:
            user["ismi"] = updatea.ismi

            user["yoshi"] = updatea.yoshi
    return f"{user_id}fgjh"
@app.delete("/a/delete/{user_id}")
def updatea(user_id:int, updatea:usern):
    for user in users:
        if user["id"]  ==user_id:
            user["ismi"] = updatea.ismi

            user["yoshi"] = updatea.yoshi
    return f"{user_id}fgjh"