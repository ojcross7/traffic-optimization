import psycopg2  
from config import settings  

class PostgreSQLConnector:  
    def __init__(self):  
        self.conn = psycopg2.connect(  
            dbname=settings.DB_NAME,  
            user=settings.DB_USER,  
            password=settings.DB_PASSWORD,  
            host=settings.DB_HOST  
        )  

    def insert_traffic_data(self, data):  
        query = """  
        INSERT INTO traffic_data (timestamp, vehicle_count, speed, location)  
        VALUES (%s, %s, %s, %s)  
        """  
        with self.conn.cursor() as cur:  
            cur.execute(query, (  
                data["timestamp"],  
                data["vehicle_count"],  
                data["speed"],  
                data["location"]  
            ))  
        self.conn.commit()  