import redis  
import json  

class RedisConnector:  
    def __init__(self, host='localhost', port=6379):  
        self.client = redis.Redis(host=host, port=port)  

    def cache_traffic_data(self, key, data):  
        """Store real-time data with a 5-minute TTL."""  
        self.client.setex(key, 300, json.dumps(data))  

    def get_cached_data(self, key):  
        """Retrieve data from Redis."""  
        data = self.client.get(key)  
        return json.loads(data) if data else None  