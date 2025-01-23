from fastapi import FastAPI
from pydantic import BaseModel
from phishing_detection import load_model, extract_features, predict

# Initialize FastAPI app
app = FastAPI()

# Load the trained model
model = load_model()

# Define the request model
class URLInput(BaseModel):
    url: str

@app.post("/predict/")
def predict_url(data: URLInput):
    """API Endpoint to predict whether a URL is phishing or legitimate."""
    features = extract_features(data.url)  # Extract features from URL
    prediction = predict(model, features)  # Get prediction (1 = phishing, 0 = legitimate)

    # Return response as a JSON dictionary
    return {
        "url": data.url,
        "phishing": bool(prediction)  # Convert prediction to True/False
    }
