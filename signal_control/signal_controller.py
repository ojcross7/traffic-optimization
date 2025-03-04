class SignalController:  
    def __init__(self, intersection_id):  
        self.intersection_id = intersection_id  
        self.current_green = 30  # Default green time (seconds)  

    def adjust_green_time(self, vehicle_count, congestion_level):  
        """Adjust green time based on vehicle count and congestion prediction."""  
        if congestion_level > 0.7:  
            self.current_green = min(60, self.current_green + 10)  # Extend green  
        elif vehicle_count < 10:  
            self.current_green = max(20, self.current_green - 5)  # Reduce green  
        return self.current_green  

    def emergency_override(self, emergency_type):  
        """Prioritize emergency vehicles."""  
        if emergency_type == "ambulance":  
            self.current_green = 60  # Force green for 60 seconds  
        return self.current_green  