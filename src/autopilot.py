import krpc
import time

from src.util import clear_screen
from src.data import OrbitData, VesselData

class KSPAutopilot:
    
    def __init__(
        self, 
        name="Automated Launch Program",
        sas = True,
        rcs = False,
        throttle = 1.0):
        
        self._conn = krpc.connect(name=name)
        # Converting useful KRPC interactions for readability
        self._vessel = self._conn.space_center.active_vessel # type: ignore
        self._vessel_ref_frame = self._vessel.reference_frame
              
        # Object defaults
        self._name = name
        self._sas = sas
        self._rcs = rcs
        self._throttle = throttle
        
        # In-Game default sync
        self._vessel.control.throttle = self._throttle
        self._vessel.control.sas = self._sas
        self._vessel.control.rcs = self._rcs
        
        # Data streams
        self._flight_data = self._conn.add_stream(self._vessel.flight, self._vessel_ref_frame)
    
    # Vessel Control
    def next_stage(self):
        """
        Activates the next stage of the vessel and returns a list of discarded parts and the number of parts discarded
        """
        discarded_parts = self._vessel.control.activate_next_stage()
        part_count = len(discarded_parts)
        return part_count, discarded_parts
    
    def enable_autopilot(self):
        self._vessel.auto_pilot.engage()
        
    def enable_sas(self):
        self._sas = True
        self._vessel.auto_pilot.sas = True
        
    def disable_sas(self):
        self._sas = False
        self._vessel.auto_pilot.sas = False
        
    def disable_autopilot(self):
        self._vessel.auto_pilot.disengage()
        self._vessel.auto_pilot.sas = self._sas

    def set_pitch(self, target_pitch):
        self._vessel.auto_pilot.target_pitch = target_pitch
        
    def set_heading(self, target_heading):
        self._vessel.auto_pilot.target_heading = target_heading
                
    def set_roll(self, target_roll):
        self._vessel.auto_pilot.target_roll = target_roll

    # Data retrieval
    def get_vessel_data(self):
        flight_info = self._vessel.flight()
        orbit_info = self._vessel.orbit
        mean_alt = self._conn.add_stream(getattr, flight_info, "mean_altitude")
        surf_alt = self._conn.add_stream(getattr, flight_info, "surface_altitude")
        speed = self._conn.add_stream(getattr, flight_info, "speed")
        orbital_body = self._conn.add_stream(getattr, orbit_info, "body")
        orbital_speed = None
        orbital_period = None
        orbital_inclination = None
        apoapsis = None
        periapsis = None
        time_to_apoapsos = None
        time_to_periapsis = None
        
        return f"{orbital_body()}"

    # QoL
    def countdown(self, seconds, activate_stage=True, string="Launching in"):
        """
        Prints countdown to console and activates stage by default.
        """
        for i in range(seconds, 0, -1):
            print(f"{string} {i}...")
            time.sleep(1)
        if activate_stage:
            self.next_stage()
            