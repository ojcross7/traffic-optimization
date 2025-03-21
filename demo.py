import requests

# Test congestion prediction
prediction = requests.post(
    "http://localhost:5000/predict",
    json={"hour": 18, "day": 4, "vehicle_count_norm": 2.1, "speed_norm": -1.0},
).json()
print(f"Congestion Prediction: {prediction}")

# Test signal control
signal_time = requests.post(
    "http://localhost:5000/signal", json={"vehicle_count": 42}
).json()
print(f"Adjusted Green Time: {signal_time} seconds")
