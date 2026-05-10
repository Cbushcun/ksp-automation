# KSP Automation

A lightweight Kerbal Space Program automation project built with Python and the KRPC mod. This repository demonstrates a simple autopilot architecture, terminal-based telemetry output, and integration with KSP using remote procedure calls.

## Project Overview

This project connects to a running Kerbal Space Program game through the KRPC protocol and provides:

- Real-time vessel telemetry printing in the terminal
- Basic autopilot controls for staging, pitch, heading, and SAS
- Colored terminal output and in-place screen refresh for smooth updates
- Structured data models for vessel and orbit information

## What’s Included

- `main.py` — entry point for the automation script
- `requirements.txt` — Python dependencies for KRPC and protobuf
- `src/autopilot.py` — `KSPAutopilot` class wrapping KRPC commands
- `src/data.py` — `VesselData` and `OrbitData` objects for readable output
- `src/util.py` — terminal helpers for screen clearing and colored text

## Technologies & Skills

- Python 3
- KRPC integration with Kerbal Space Program
- Terminal UI techniques using ANSI escape codes
- Object-oriented design for automation and telemetry
- Dependency management using `requirements.txt`
- Data modeling and clean code structure

## Requirements

- Kerbal Space Program installed
- KRPC mod installed and running inside KSP
- Python 3.11+ (or Python 3.10+) installed
- `krpc` and `protobuf` Python packages

## Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/ksp-automation.git
cd ksp-automation
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Launch Kerbal Space Program and start the KRPC server inside the game.

## Usage

Run the automation script with:

```bash
python3 main.py
```

If KSP and the KRPC connection are available, the script will:

- connect to the active vessel
- stage once immediately
- print vessel and orbit data continuously
- enable autopilot and set a heading/pitch when the vessel reaches ~50 m/s

## Code Structure

### `main.py`

- Initializes `KSPAutopilot`
- Clears the terminal each frame using `clear_screen()`
- Prints live vessel and orbit data
- Triggers basic autopilot behavior at a target speed

### `src/autopilot.py`

- Connects to KSP using `krpc.connect()`
- Wraps KRPC control and autopilot functions
- Provides methods for `next_stage()`, `enable_autopilot()`, `set_pitch()`, `set_heading()`, and more
- Retrieves structured telemetry through `get_vessel_data()` and `get_orbit_data()`

### `src/data.py`

- Defines `VesselData` and `OrbitData` classes
- Rounds and formats telemetry values for better readability
- Uses `__repr__()` to produce clean terminal output

### `src/util.py`

- Provides terminal helpers:
  - `clear_screen()` — resets the terminal viewport
  - `color_str()` — adds ANSI color formatting to status labels

## Notes for Hiring Managers

This project highlights:

- practical automation of a simulation environment
- working knowledge of remote APIs and game integration
- clean separation of concerns across modules
- terminal-based UX improvements to avoid flashing output
- ability to document setup and architecture for collaborators

## Troubleshooting

- Ensure the KRPC server is active in KSP before running `main.py`
- Verify that Python is using the same network interface accessible to KSP
- If output is not visible, check that your terminal supports ANSI escape codes

---

Happy launching!
