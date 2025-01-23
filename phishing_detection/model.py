import pickle
import pandas as pd

def load_model(model_path="XGBoostClassifier.pickle.dat"):
    """Load the saved XGBoost model from a file."""
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model

def predict(model, features_df):
    """Predict phishing or legitimate URL."""
    prediction = model.predict(features_df)
    return prediction[0]
