import unittest  
import numpy as np  
from data_processing.ml_models.lstm_model import TrafficPredictor  

class TestMLModels(unittest.TestCase):  
    def test_lstm_prediction(self):  
        model = TrafficPredictor()  
        dummy_data = np.random.rand(24, 3)  # 24 timesteps, 3 features  
        prediction = model.predict(dummy_data)  
        self.assertTrue(0 <= prediction <= 1)  