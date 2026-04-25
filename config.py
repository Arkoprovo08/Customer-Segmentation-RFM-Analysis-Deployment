import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

scaler = joblib.load(os.path.join(BASE_DIR, "artifacts/scaler.pkl"))
kmeans = joblib.load(os.path.join(BASE_DIR, "artifacts/kmeans.pkl"))
quantiles = joblib.load(os.path.join(BASE_DIR, "artifacts/quantiles.pkl"))