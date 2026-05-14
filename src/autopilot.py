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
        self._ref_frame = self._vessel.reference_frame
        
        # Data Streams
        self._flight_stream = self._conn.add_stream(self._vessel.flight, self._ref_frame)        
        # Defaults
        self._name = name
        self._sas = sas
        self._rcs = rcs
        self._throttle = throttle
        
        # Configuring defaults
        self._vessel.control.throttle = self._throttle
        self._vessel.control.sas = self._sas
        self._vessel.control.rcs = self._rcs
    
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
        
    def enable_rcs(self):
        self._rcs = True
        # self._vessel.auto_pilot.rcs
        
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
            
    # Data Retrieval
    def get_vessel_data(self):
        """Returns a VesselData object containing the current vessel data"""
        orbital_reference_frame = self._vessel.orbit.body.reference_frame
        info = self._vessel.control
        flight_info = self._flight_stream()
        orbital_flight_info = self._conn.add_stream(self._vessel.flight, orbital_reference_frame)    
        return VesselData(
            sas_status = info.sas,
            rcs_status = info.rcs,
            pitch = flight_info.pitch, # type: ignore
            heading = flight_info.heading, # type: ignore
            roll = flight_info.roll, # type: ignore
            throttle = info.throttle,
            speed = orbital_flight_info().speed, # type: ignore
            velocity = flight_info.velocity, # type: ignore
            mean_altitude = flight_info.mean_altitude, # type: ignore
            surface_altitude = flight_info.surface_altitude, # type: ignore
            solar_panel_status = info.solar_panels
        )
        
    def get_orbit_data(self):
        """Returns an OrbitData object containing the current orbital data"""
        orbit = self._vessel.orbit
        return OrbitData(
            body = orbit.body.name,
            speed = orbit.speed,
            period = orbit.period,
            apoapsis = orbit.apoapsis,
            periapsis = orbit.periapsis,
            time_to_apoapsis = orbit.time_to_apoapsis,
            time_to_periapsis = orbit.time_to_periapsis
        )
