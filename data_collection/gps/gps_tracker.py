import random  
from datetime import datetime  

class GPSTracker:  
    def __init__(self, vehicle_id):  
        self.vehicle_id = vehicle_id  

    def generate_location(self):  
        """Simulate GPS coordinates (Accra bounding box)."""  
        return {  
            "timestamp": datetime.now().isoformat(),  
            "vehicle_id": self.vehicle_id,  
            "latitude": random.uniform(5.5, 5.7),  
            "longitude": random.uniform(-0.4, 0.1)  
        }  

if __name__ == "__main__":  
    tracker = GPSTracker("GH-ABC-123")  
    print(tracker.generate_location())  