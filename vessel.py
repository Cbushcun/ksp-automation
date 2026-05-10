import krpc
import time


from util import clear_screen

class Vessel:
    
    def __init__(self, name="Orbital Flight"):
        self._name = name
        self._conn = krpc.connect(name=name)
        self._vessel = self._conn.space_center.active_vessel # type: ignore
        self._sas = True
        self._rcs = False
        self._throttle = 1.0
        self._max_throttle = 1.0
        self._velocity = 0
        self._autopilot = False
        self._pitch = 90
        self._heading = 90
        
        self._vessel.control.sas = self._sas
        self._vessel.control.rcs = self._rcs
        self._vessel.control.throttle = self._throttle
        self._vessel.auto_pilot.target_pitch_and_heading(self._pitch, self._heading)
        
    # Vessel Automations
    def activate_next_stage(self):
        """
        Activates the next stage of the vessel and prints the 
        """
        print("Activating next stage...")
        discarded_parts = self._vessel.control.activate_next_stage()
        part_count = len(discarded_parts)
        return {"count": part_count, "parts": discarded_parts}
    
    def engage_autopilot(self):
        """
        Toggles the autopilot control to allow vessle adjustments via python code. Autopilot activation automatically deactivates sas.
        """
        self._vessel.auto_pilot.engage()
        self._autopilot = True
        self._sas = False
        return self._autopilot
    
    def disengage_autopilot(self):
        """
        Disengages autopilot control and returns control to the player. Autopilot deactivation automatically reactivates sas.
        """
        self._vessel.auto_pilot.disengage()
        self._autopilot = False
        self._sas = True
        self._vessel.control.sas = self._sas
        return self._autopilot
    
    # Booleans
    def toggle_rcs(self):
        """
        Toggles the rcs value for the vehicle and returns it as a boolean value.
        """
        self._rcs = not self._rcs
        self._vessel.control.rcs = self._rcs
        return self._rcs
    
    def toggle_sas(self):
        """
        Toggles the sas value for the vehichle and returns it as a boolean value.
        """
        self._sas = not self._sas
        self._vessel.control.sas = self._sas
        return self._sas
    
    def toggle_throttle(self):
        """
        Toggles the currnet throttle on or off. If current throttle is anything but 0, it will be set to 0. Otherwise, it will be returned to its previous throttle value.
        """
        
        self._max_throttle = self._throttle  
    
    # Getters
    def get_autopilot(self):
        return self._autopilot
    
    def get_velocity(self):
        return self._vessel.flight(self._vessel.orbit.body.reference_frame).speed
    
    def get_pitch_and_yaw(self):
        pitch = self._vessel.flight().pitch
        yaw = self._vessel.flight().heading
        return pitch, yaw
    
    def get_sas(self):
        return self._sas
    
    def get_rcs(self):
        return self._rcs
    
    def get_throttle(self):
        return self._throttle
    
    def get_fuel_level(self, resource="SolidFuel"):
        fuel_level = (self._vessel.resources.amount(resource) / self._vessel.resources.max(resource)) * 100
        return round(fuel_level, 2)
    
    def get_thrust(self):
        thrust = self._vessel.thrust
        return round(thrust, 2)
    
    def get_altitude(self):
        altitude = self._vessel.flight().mean_altitude
        return round(altitude, 2)
    
    # Setters
    def set_pitch(self, pitch, deviation = 1):
        """
        Sets vehicle object pitch and returns dict of current pitch and heading.
        """
        if not self._autopilot:
            self._autopilot = self.engage_autopilot()
        self._pitch = pitch
        self._vessel.auto_pilot.target_pitch_and_heading(self._pitch, self._heading)
        self._pitch, self._yaw = self.get_pitch_and_yaw()
        
    def set_heading(self, heading):
        """
        Sets vehicle object heading.
        """
        if not self._autopilot:
            print("Autopilot is not engaged. Heading will be set once autopilot is engaged.")
            self._autopilot = self.engage_autopilot()
            time.sleep(1)
            print(f"Autopilot engaged")
        self._heading = heading
        self._vessel.auto_pilot.target_pitch_and_heading(self._pitch, self._heading)
        time.sleep(1)
        print(f"Heading set to {self._heading}")
    
    def set_throttle(self, throttle):
        """
        Sets vehicle throttle to provided float value.
        """
        self._throttle = throttle
        self._vessel.control.throttle = throttle
        
    # QoL Methods
    def countdown(self, seconds, activate_stage=False, string="Launching in"):
        for i in range(seconds, 0, -1):
            print(f"{string} {i}...")
            time.sleep(1)
        if activate_stage:
            self.activate_next_stage()