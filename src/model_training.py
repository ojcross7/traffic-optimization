import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib


def train_and_save_model():
    """Train and save traffic congestion prediction model"""
    # Load processed data
    processed_df = pd.read_csv("../data/processed/processed_data.csv")

    # Prepare features/target
    features = processed_df[["hour", "day", "vehicle_count_norm", "speed_norm"]]
    target = processed_df["congestion"]

    # Split data (using more descriptive names)
    features_train, features_test, target_train, target_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )

    # Train model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(features_train, target_train)

    # Evaluate model (optional)
    test_accuracy = model.score(features_test, target_test)
    print(f"Model test accuracy: {test_accuracy:.2f}")

    # Save model
    os.makedirs("../models", exist_ok=True)
    joblib.dump(model, "../models/traffic_model.pkl")


if __name__ == "__main__":
    train_and_save_model()
