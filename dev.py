import krpc
import time

from src.util import clear_screen
from src.autopilot import KSPAutopilot

# conn = krpc.connect()
# vessel = conn.space_center.active_vessel
# refframe = vessel.orbit.body.reference_frame
# position = conn.add_stream(conn.space_center.active_vessel.flight, refframe)
ap = KSPAutopilot()

while True:
    clear_screen()
    print(ap.get_vessel_data())
    time.sleep(0.1)