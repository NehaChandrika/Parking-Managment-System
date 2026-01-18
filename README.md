Multi-Level Parking System Projects      🚗

This repository contains three Python parking system projects, each improving on the previous one:

Single-Line Parking System:
Vehicles are parked in a single row of slots.
Users can park, remove, and check if a slot is available.

Single-Floor Parking System:
Vehicles are parked in a grid layout (rows × columns) on one floor.
Users can park, remove, and view the parking layout.

Multi-Level Parking System:
Vehicles are parked across multiple floors, each with rows and columns.
Users can park, remove, and see the parking layout of all floors.

Table of Contents
Features
How Each Project Works
Example Usage
How to Run
Progression Summary

Features
Park and remove vehicles efficiently.
Prevent duplicate vehicle entries.
Check availability of parking slots.
Display parking slots in a 1D line, 2D grid, or multi-level structure.
Handles full parking scenarios gracefully.

How Each Project Works
1. Single-Line Parking System
   User inputs the total number of parking slots.
   Parking slots are stored in a 1D list, where 0 indicates empty.

Commands:
in → Park a vehicle at the first available slot.
out → Remove a vehicle.
Exit → Quit the program.

2. Single-Floor Parking System
   User inputs the number of rows and columns.
   Parking slots are stored as a 2D list (rows × columns).

Commands:
in → Park a vehicle at the first available slot.
out → Remove a vehicle.
display → Show the parking layout of the floor.
exit → Quit the program.

3. Multi-Level Parking System
   User inputs the number of floors, rows, and columns.
   Parking slots are stored as a 3D list (floors × rows × columns).

Commands:
in → Park a vehicle at the first available slot across all floors.
out → Remove a vehicle.
display → Show the parking layout of all floors.
exit → Quit the program         

How to Run
   Ensure Python 3 is installed.
   Open Terminal/Command Prompt.
   Navigate to the folder containing the .py file.

Run the code:

python single_line_parking.py
python single_floor_parking.py
python multi_level_parking.py


