from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import joblib

app = FastAPI()

# Enable CORS for all origins (for testing locally)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your model
model = joblib.load("model.pkl")

class Features(BaseModel):
    features: List[float]

@app.get("/")
def home():
    return {"message": "ML Model API is running!"}

@app.post("/predict")
def predict(data: Features):
    if len(data.features) != 12:
        return {"error": "You must provide exactly 12 features in order."}
    try:
        prediction = model.predict([data.features])
        return {"prediction": prediction.tolist()}
    except Exception as e:
        return {"error": str(e)}
