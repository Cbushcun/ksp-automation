import krpc
import time

from src.util import clear_screen
from src.data.orbit import OrbitData
from src.data.vessel import VesselData

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
        self._ref_frame = self._vessel.surface_reference_frame
        self._flight_telemetry = self._vessel.flight(self._vessel.surface_reference_frame)
        
        # Initiating local object data
        self._name = name
        self._sas = sas
        self._rcs = rcs
        self._throttle = throttle
        
        # Configuring KRPC controller defaults
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
        """
        Toggles the currnet throttle on or off. If current throttle is anything but 0, it will be set to 0. Otherwise, it will be returned to its previous throttle value.
        """
        self._max_throttle = self._throttle  
    
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
            
    # Getter Methods
    def get_vessel_data(self):
        """Returns a VesselData object containing the current vessel data"""
        info = self._vessel.control
        control_info = self._vessel.control
        flight_info = self._vessel.flight(self._ref_frame)
        
        return VesselData(
            sas_status = info.sas,
            rcs_status = info.rcs,
            pitch = flight_info.pitch,
            heading = flight_info.heading,
            roll = flight_info.roll,
            throttle = info.throttle,
            thrust = self._vessel.thrust,
            speed = flight_info.speed,
            velocity = flight_info.velocity,
            mean_altitude = flight_info.mean_altitude,
            surface_altitude = flight_info.surface_altitude,
            solar_panel_status = control_info.solar_panels
        )
    
    def get_orbit_data(self):
        """Returns an OrbitData object containing the current orbital data"""
        orbit = self._vessel.orbit
        return OrbitData(
            body = orbit.body,
            speed = orbit.speed,
            period = orbit.period,
            apoapsis = orbit.apoapsis,
            periapsis = orbit.periapsis,
            time_to_apoapsis = orbit.time_to_apoapsis,
            time_to_periapsis = orbit.time_to_periapsis
        )
    
    # Setters
