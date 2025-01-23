from fastapi import FastAPI
from phishing_detection.model import load_model, predict
from phishing_detection.features import extract_features

app = FastAPI()

model = load_model("XGBoostClassifier.pickle.dat")

@app.post("/predict/")
def predict_url(url: str):
    features = extract_features(url)
    prediction = predict(model, features)
    return {"url": url, "phishing": bool(prediction)}
