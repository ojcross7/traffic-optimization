import random  
import time  
from datetime import datetime  

class WeatherSensor:  
    def __init__(self, sensor_id, location):  
        self.sensor_id = sensor_id  
        self.location = location  

    def generate_data(self):  
        """Simulate weather data (temperature in °C, rainfall in mm)."""  
        return {  
            "timestamp": datetime.now().isoformat(),  
            "sensor_id": self.sensor_id,  
            "temperature": random.uniform(20, 35),  
            "rainfall": random.uniform(0, 10),  
            "visibility": random.choice(["clear", "foggy", "rainy"])  
        }  

if __name__ == "__main__":  
    sensor = WeatherSensor("W001", "Intersection_A")  
    while True:  
        print(sensor.generate_data())  
        time.sleep(60)  # Emit data every 60 seconds  