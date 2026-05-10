import time

from util import clear_screen
from vessel import Vessel

if __name__ == "__main__": 
    rocket = Vessel()
    current_velocity = 0
    countdown_time = 5
    
    rcs_status = rocket.get_rcs()
    sas_status = rocket.get_sas()
    if not sas_status:
        rocket.toggle_sas()
    rocket.countdown(countdown_time, activate_stage=True)
    time.sleep(1)
    while True:
       print(rocket._velocity)
        