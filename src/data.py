from src.util import color_str

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
        self.pitch = round(pitch)
        self.heading = round(heading)
        self.roll = round(roll)
        self.throttle = round(throttle, 2) * 100
        self.thrust = thrust
        self.speed = round(speed, 1)
        self.velocity = velocity
        self.mean_altitude = round(mean_altitude)
        self.surface_altitude = round(surface_altitude)
        self.solar_panel_status = solar_panel_status
        
    def __repr__(self):
        return f"""======Current Vessel Data======
    Pitch/Heading/Roll: {self.pitch} / {self.heading} / {self.roll}
    Throtle: {color_str(str(self.throttle), "green" if self.throttle > 0 else "red")}%
    Thrust: {self.thrust}
    Speed: {self.speed}m/s
    Velocity: {self.velocity}
    Altitude (Sea-Level): {self.mean_altitude}m
    Altitude (Surface): {self.surface_altitude}m
    SAS: {color_str("ACTIVE", "green") if self.sas_status else color_str("INACTIVE", "red")}
    RCS: {color_str("ACTIVE", "green") if self.rcs_status else color_str("INACTIVE", "red")}
    Solar Panels: {color_str("ACTIVE", "green") if self.solar_panel_status else color_str("INACTIVE", "red")}"""
    
class OrbitData:
    def __init__(
        self,
        body,
        speed,
        period,
        apoapsis,
        periapsis,
        time_to_apoapsis,
        time_to_periapsis
    ):
        self.body = body
        self.speed = round(speed, 1)
        self.period = round(period, 2)
        self.apoapsis = round(apoapsis)
        self.periapsis = round(periapsis)
        self.time_to_apoapsis = round(time_to_apoapsis)
        self.time_to_periapsis = round(time_to_periapsis)
        
    def __repr__(self):
        return f"""======Current Orbit Data======
    Body: {self.body}
    Speed: {self.speed}m/s
    Period: {self.format_time(self.period)}
    Apoapsis: {self.apoapsis}m (T- {self.format_time(self.time_to_apoapsis)})
    Periapsis: {self.periapsis}m (T- {self.format_time(self.time_to_periapsis)})"""
    
    def format_time(self, seconds):
        minutes = round(seconds // 60)
        remaining_seconds = round(seconds % 60)
        return f"{minutes}m {remaining_seconds}s"