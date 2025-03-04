from sklearn.ensemble import IsolationForest  
import numpy as np  

class AnomalyDetector:  
    def __init__(self, contamination=0.05):  
        self.model = IsolationForest(contamination=contamination)  

    def train(self, historical_data):  
        """Train on historical traffic data (vehicle counts, speeds)."""  
        self.model.fit(historical_data)  

    def detect(self, real_time_data):  
        """Predict anomalies (1 = normal, -1 = anomaly)."""  
        prediction = self.model.predict(real_time_data.reshape(1, -1))  
        return prediction[0] == -1  