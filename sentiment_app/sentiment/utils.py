import os
import pickle
from django.conf import settings

# Path to the model and vectorizer
MODEL_PATH = os.path.join(settings.BASE_DIR, 'ml_Models', 'sentiment_model.pkl')

try:
    with open(MODEL_PATH, 'rb') as f:
        vectorizer, model = pickle.load(f)
except FileNotFoundError:
    raise Exception(f"Model file not found at {MODEL_PATH}")

def classify_sentiment(text):
    X = vectorizer.transform([text])
    return model.predict(X)[0]
