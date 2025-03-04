import numpy as np  
import tensorflow as tf  
from tensorflow.keras.models import Sequential  
from tensorflow.keras.layers import LSTM, Dense  

class TrafficPredictor:  
    def __init__(self, input_shape=(24, 3)):  # 24 timesteps, 3 features  
        self.model = self.build_model(input_shape)  

    def build_model(self, input_shape):  
        model = Sequential([  
            LSTM(64, input_shape=input_shape, return_sequences=True),  
            LSTM(32),  
            Dense(1)  # Predict congestion level (0-1)  
        ])  
        model.compile(loss="mse", optimizer="adam")  
        return model  

    def train(self, X_train, y_train, epochs=50):  
        self.model.fit(X_train, y_train, epochs=epochs)  

    def predict(self, data):  
        return self.model.predict(np.expand_dims(data, axis=0))[0][0]  