import joblib

# Load pre-trained model
model = joblib.load("models/accident_model.pkl")

def predict_risk(data):
    features = [data['latitude'], data['longitude'], data['hour']]  # Simplified
    return model.predict([features])[0]