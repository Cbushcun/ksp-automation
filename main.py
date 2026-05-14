import time

from src.util import clear_screen
from src.autopilot import KSPAutopilot

if __name__ == "__main__": 
    rocket = KSPAutopilot()
    vessel_data = rocket._conn.add_stream(rocket.get_vessel_data)
        