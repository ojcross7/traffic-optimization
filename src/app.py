"""Flask API for traffic prediction and signal control"""

from flask import Flask, jsonify, request
import os
import joblib
import pandas as pd
from src.signal_control import adjust_signal_cycle  # Correct import path
from flask_httpauth import HTTPTokenAuth
import logging
from logging.handlers import RotatingFileHandler
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from prometheus_client import start_http_server, Counter, generate_latest

app = Flask(__name__)
model = joblib.load("models/traffic_model.pkl")  # Path relative to project root


@app.route("/predict", methods=["POST"])
def predict_congestion():
    """Predict congestion status from input data"""
    data = request.json
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return jsonify({"congestion": int(prediction)})


@app.route("/signal", methods=["POST"])
def control_signal():
    """Calculate optimal green time for signals"""
    vehicle_count = request.json.get("vehicle_count")
    return jsonify({"green_time": adjust_signal_cycle(vehicle_count)})


auth = HTTPTokenAuth(scheme="Bearer")


@auth.verify_token
def verify_token(token):
    return token == os.getenv("API_SECRET_KEY")


@app.route("/admin")
@auth.login_required
def admin_panel():
    return jsonify(...)


REQUEST_COUNT = Counter("api_requests", "Total API requests")


@app.route("/metrics")
def metrics():
    return generate_latest()


# Logging config
handler = RotatingFileHandler("traffic.log", maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)


@app.route("/predict")
def predict():
    app.logger.info("Prediction request received")
    ...


limiter = Limiter(app=app, key_func=get_remote_address)


@app.route("/predict")
@limiter.limit("10/minute")
def predict(): ...


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
