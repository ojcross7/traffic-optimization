import cv2  
import numpy as np  
from datetime import datetime  

class VideoProcessor:  
    def __init__(self, camera_id):  
        self.camera_id = camera_id  
        self.background_subtractor = cv2.createBackgroundSubtractorMOG2()  

    def process_frame(self, frame):  
        """Detect vehicles using background subtraction."""  
        fg_mask = self.background_subtractor.apply(frame)  
        contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  
        vehicle_count = 0  

        for contour in contours:  
            if cv2.contourArea(contour) > 500:  # Filter small contours  
                vehicle_count += 1  

        return {  
            "timestamp": datetime.now().isoformat(),  
            "camera_id": self.camera_id,  
            "vehicle_count": vehicle_count  
        }  

if __name__ == "__main__":  
    # Example usage with OpenCV video capture  
    cap = cv2.VideoCapture("traffic_video.mp4")  
    processor = VideoProcessor("CAM_001")  

    while cap.isOpened():  
        ret, frame = cap.read()  
        if not ret:  
            break  
        data = processor.process_frame(frame)  
        print(data)  