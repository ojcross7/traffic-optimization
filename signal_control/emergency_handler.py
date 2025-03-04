class EmergencyHandler:  
    def __init__(self):  
        self.active_emergencies = {}  

    def register_emergency(self, vehicle_id, emergency_type, location):  
        """Track emergency vehicles (e.g., ambulances, fire trucks)."""  
        self.active_emergencies[vehicle_id] = {  
            "type": emergency_type,  
            "location": location,  
            "timestamp": datetime.now().isoformat()  
        }  

    def clear_emergency(self, vehicle_id):  
        """Remove resolved emergencies."""  
        if vehicle_id in self.active_emergencies:  
            del self.active_emergencies[vehicle_id]  