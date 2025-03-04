import random  
import time  
from datetime import datetime  

class TrafficSensor:  
    def __init__(self, sensor_id, location):  
        self.sensor_id = sensor_id  
        self.location = location  

    def generate_data(self):  
        """Simulate real-time traffic data."""  
        return {  
            "timestamp": datetime.now().isoformat(),  
            "sensor_id": self.sensor_id,  
            "vehicle_count": random.randint(0, 100),  
            "speed": random.uniform(0, 60),  # km/h  
            "queue_length": random.randint(0, 20)  
        }  

if __name__ == "__main__":  
    sensor = TrafficSensor("S001", "Intersection_A")  
    while True:  
        print(sensor.generate_data())  
        time.sleep(5)  # Emit data every 5 seconds  