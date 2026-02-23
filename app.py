from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI
class UserAdd(BaseModel):
    model: str
    turi: str
    narxi_Ozbekistonda: str
    dvigatel_hajmi: str
    ot_kuchi: str
    maksimal_tezlik: str
    yoqilgi_sarfi: str
    uzunligi: str
    kengligi: str
userlar = [{
        "model": "Toyota Corolla",
        "turi": "Sedan",
        "narxi_Ozbekistonda": "taxminan 250 975 000 so'm",
        "dvigatel": "1.2L Turbo, 116 ot kuchi, CVT",
        "maksimal_tezlik": "taxminan 180 km/soat",
        "yoqilgi_sarfi": "taxminan 5.7–6.0 litr / 100 km",
        "uzunligi": "4635 mm",
        "kengligi": "1780 mm"
}]
@app.get("/allitems")
def allitems():
    return userlar
@app.post("/allitems/add")
def addAllitems(user:UserAdd):
    userlar.append(user)