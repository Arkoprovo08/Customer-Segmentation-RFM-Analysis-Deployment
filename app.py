from fastapi import FastAPI
from model import predict_segment

app = FastAPI(title="RFM Customer Segmentation API")


@app.get("/")
def home():
    return {"message": "RFM Segmentation API is running"}


@app.get("/predict")
def predict(recency: float, frequency: float, monetary: float):
    
    result = predict_segment(recency, frequency, monetary)
    
    return result