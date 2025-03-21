import pandas as pd
import numpy as np
import os

def generate_raw_data(save_path="../data/raw/raw_traffic_data.csv"):
    # Generate synthetic raw data
    timestamps = pd.date_range(start="2024-01-01", periods=1000, freq="5min")
    vehicle_count = np.random.randint(0, 100, 1000)
    speed = np.random.uniform(0, 60, 1000)
    
    raw_df = pd.DataFrame({
        "timestamp": timestamps,
        "vehicle_count": vehicle_count,
        "speed": speed
    })
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    raw_df.to_csv(save_path, index=False)
    return raw_df

def preprocess_data(raw_df, save_path="../data/processed/processed_data.csv"):
    # Clean and normalize data
    df = raw_df.copy()
    df["hour"] = df["timestamp"].dt.hour
    df["day"] = df["timestamp"].dt.dayofweek
    df["vehicle_count_norm"] = (df["vehicle_count"] - df["vehicle_count"].mean()) / df["vehicle_count"].std()
    df["speed_norm"] = (df["speed"] - df["speed"].mean()) / df["speed"].std()
    df["congestion"] = np.where(df["vehicle_count"] > 50, 1, 0)  # Add target variable
    
    # Save processed data
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)
    return df

if __name__ == "__main__":
    # Generate and save raw + processed data
    raw_data = generate_raw_data()
    processed_data = preprocess_data(raw_data)