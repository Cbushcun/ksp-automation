import time

from src.util import clear_screen
from src.autopilot import KSPAutopilot

if __name__ == "__main__": 
    rocket = KSPAutopilot()
    current_velocity = 0
    countdown_time = 5
    rocket.next_stage()
    while True:
        clear_screen()
        rocket_data = rocket.get_vessel_data()
        orbit_data = rocket.get_orbit_data()
        print(rocket_data)
        print(orbit_data)
        if 49 <= rocket_data.speed <= 51:
            rocket.enable_autopilot()
            rocket.set_heading(90)
            rocket.set_pitch(45)
        time.sleep(0.01)
        