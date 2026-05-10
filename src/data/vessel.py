class VesselData:
    def __init__(
        self,
        sas_status,
        rcs_status,
        pitch,
        heading,
        roll,
        throttle,
        thrust,
        speed,
        velocity,
        mean_altitude,
        surface_altitude,
        solar_panel_status
    ):
        self.sas_status = sas_status
        self.rcs_status = rcs_status
        self.pitch = pitch
        self.heading = heading
        self.roll = roll
        self.throttle = throttle
        self.thrust = thrust
        self.speed = speed
        self.velocity = velocity
        self.mean_altitude = mean_altitude
        self.surface_altitude = surface_altitude
        self.solar_panel_status = solar_panel_status
        
    def __repr__(self):
        return f"""======Current Vessel Data======
    SAS: {"ACTIVE" if self.sas_status else "INACTIVE"}
    RCS: {"ACTIVE" if self.rcs_status else "INACTIVE"}
    Pitch/Heading/Roll: {self.pitch}/{self.heading}/{self.roll}
    Throtle: {self.throttle}
    Thrust: {self.thrust}
    Speed: {self.speed}m/s
    Velocity: {self.velocity}
    Altitude (Sea-Level): {self.mean_altitude}
    Altitude (Surface): {self.surface_altitude}
    Solar Panels: {"ACTIVE" if self.solar_panel_status else "INACTIVE"}"""
