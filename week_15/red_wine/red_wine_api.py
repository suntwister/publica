from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import uvicorn
import numpy as np
import pandas as pd

model = joblib.load("BestModel.pkl")
scaler = joblib.load("encoder.pkl")

app = FastAPI()

class redwinefeatures(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

@app.get("/")
def root():
    return "Welcome to Red wine app"

@app.post("/predict")
def predict(wine: redwinefeatures):
    features = np.array([[
        wine.fixed_acidity,
        wine.volatile_acidity,
        wine.citric_acid,
        wine.residual_sugar,
        wine.chlorides,
        wine.free_sulfur_dioxide,
        wine.total_sulfur_dioxide,
        wine.density,
        wine.pH,
        wine.sulphates,
        wine.alcohol
    ]])

    encoder = joblib.load("encoder.pkl")
    model = joblib.load("BestModel.pkl")

    scaled_features =  encoder.transform(features)
    prediction = model.predict(features)

    return {"prediction": str(prediction[0])}

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8080
    uvicorn.run(app, host=host, port=port)

