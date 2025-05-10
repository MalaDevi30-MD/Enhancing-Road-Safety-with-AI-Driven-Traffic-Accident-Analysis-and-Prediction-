from fastapi import APIRouter
from pydantic import BaseModel
from services.inference import predict_risk

router = APIRouter()

class AccidentInput(BaseModel):
    latitude: float
    longitude: float
    hour: int
    weather: str

@router.post("/predict")
def get_prediction(input_data: AccidentInput):
    result = predict_risk(input_data.dict())
    return {"risk_level": result}