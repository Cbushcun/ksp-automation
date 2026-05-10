import time

from src.util import clear_screen
from src.autopilot import KSPAutopilot

if __name__ == "__main__": 
    rocket = KSPAutopilot()
    current_velocity = 0
    countdown_time = 5
    
    while True:
        clear_screen()
        print(rocket.get_vessel_data())
        print(rocket.get_orbit_data())
        time.sleep(0.01)
        