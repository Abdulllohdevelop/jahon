from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI
class UserAdd(BaseModel):
    ismi:set
    yoshi:int
class UserUpdate(BaseModel):
    id:1
    ismi:set
    yoshi:int
userlar = [{
    "ismi":"abu",
    "yoshi":"12"
}]
@app.get("/allitems")
def allitems():
    return userlar
@app.post("/allitems/add")
def addAllitems(user:UserAdd):
    userlar.append(user)
    return f"{user}malumot qo'shildi"
@app.put("/allitems/update/{user_id}")
def updateAllitems(user_id:int,updateAll:UserUpdate):
    for user in userlar:
        if user["id"] == user_id:
           user["ismi"] == updateAll.ismi
           user["yoshi"] = updateAll.yoshi
           return f"{user_id}malumot"
@app.delete("/allitems/delete/{user_id}")
def deleteAllitems(user_id:int,updateAll:UserUpdate):
    for user in userlar:
        if user["id"] == user_id:
           userlar.remove(user)
           return f"{user_id}malumot"