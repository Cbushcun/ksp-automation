import time

from src.util import clear_screen
from src.autopilot import KSPAutopilot

if __name__ == "__main__": 
    rocket = KSPAutopilot()
    print(rocket.get_vessel_data())