import requests  

class RouteEngine:  
    def __init__(self, osrm_url="http://router.project-osrm.org/route/v1/driving/"):  
        self.osrm_url = osrm_url  

    def get_optimal_route(self, start, end, traffic_data):  
        """Fetch optimal route using OSRM with traffic weights."""  
        params = {  
            "coordinates": f"{start[1]},{start[0]};{end[1]},{end[0]}",  
            "annotations": "congestion",  
            "overview": "full"  
        }  
        response = requests.get(f"{self.osrm_url}", params=params)  
        return response.json()["routes"][0]["legs"][0]  