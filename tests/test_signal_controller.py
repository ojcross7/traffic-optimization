import unittest  
from signal_control.signal_controller import SignalController  

class TestSignalController(unittest.TestCase):  
    def test_adjust_green_time(self):  
        controller = SignalController("Intersection_A")  
        new_time = controller.adjust_green_time(vehicle_count=50, congestion_level=0.8)  
        self.assertEqual(new_time, 40)  # Example assertion  