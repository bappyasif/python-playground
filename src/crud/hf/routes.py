from fastapi import APIRouter, HTTPException
from src.huggingface.predict_locally import predict_locally

hf_router = APIRouter(prefix="/hf", tags=["hf"])

@hf_router.post("/predict")
async def predict(text: str):
    try:
        prediction = predict_locally(text)
        return { "prediction" : prediction }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
