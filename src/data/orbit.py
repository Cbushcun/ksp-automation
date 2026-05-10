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
        self.speed = speed
        self.period = period
        self.apoapsis = apoapsis
        self.periapsis = periapsis
        self.time_to_apoapsis = time_to_apoapsis
        self.time_to_periapsis = time_to_periapsis
        
    def __repr__(self):
        return f"""======Current Orbit Data======
    Body: {self.body}
    Speed: {self.speed}
    Period: {self.period}
    Apoapsis: {self.apoapsis}m (T-{self.time_to_apoapsis})
    Periapsis: {self.periapsis}m (T-{self.time_to_periapsis})"""
