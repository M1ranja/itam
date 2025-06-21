
from fastapi import FastAPI, HTTPException  
from app.models.asset import ITAsset
from app.services.asset_service import AssetService

app = FastAPI()
service = AssetService()

@app.get("/")
async def root():
    return {"message": "Welcome to IT Asset Management API"}

@app.post("/assets", response_model=ITAsset)
def add_asset(asset: ITAsset):
    """
    افزودن دارایی جدید
    """
    created = service.create_asset(asset)
    return created

@app.get("/assets/{id}", response_model=ITAsset)
def get_asset(id: str):
    """
    دریافت دارایی بر اساس شناسه
    """
    asset = service.get_asset(id)
    if asset:
        return asset
    raise HTTPException(status_code=404, detail="Asset not found")
