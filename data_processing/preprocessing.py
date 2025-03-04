import pandas as pd  
from sklearn.preprocessing import MinMaxScaler  
import numpy as np  

class DataPreprocessor:  
    def __init__(self):  
        self.scaler = MinMaxScaler()  

    def clean_data(self, raw_data):  
        """Clean and normalize sensor data."""  
        # Convert to DataFrame  
        df = pd.DataFrame(raw_data)  

        # Handle missing values  
        df.fillna(method='ffill', inplace=True)  

        # Normalize numerical features  
        numerical_cols = ['vehicle_count', 'speed', 'queue_length']  
        df[numerical_cols] = self.scaler.fit_transform(df[numerical_cols])  

        return df  

    def validate_data(self, data):  
        """Check for data anomalies."""  
        if data['vehicle_count'] < 0 or data['speed'] < 0:  
            raise ValueError("Invalid sensor data: negative values detected.")  
        return True  