
from keystone import keystone_mission
from leafcutter_with_elder import leafcutter_mission
from drone import drone_mission
from pybricks.parameters import Side
from rock2 import rock_mission
from rr_es import rr_es_mission
from vine import vine_mission

from pybricks.tools import hub_menu
from pybricks.hubs import PrimeHub
from robot import hub, drive_base, right_arm, wait_for_gyro, start_run
hub = PrimeHub()
hub.display.orientation(up=Side.BOTTOM)
slots = ["0", "1", "2", "3", "4", "5"]
next_index = 0

while True:
    # Rotate the list so next_index is at the front
    menu_order = slots[next_index:] + slots[:next_index]
    selected = hub_menu(*menu_order)
     # Every run starts from the same state, no matter what ran before.
    wait_for_gyro()
    start_run()
    if selected == "0":
        drive_base.straight(-70)
        right_arm.run_angle(200,-90)
        drive_base.stop
    if selected == "1":
        rock_mission()
        vine_mission()

    elif selected == "2":
        rr_es_mission()

    elif selected == "3":
        drone_mission()

    elif selected == "4":
        leafcutter_mission()

    elif selected == "5":
        keystone_mission()
    # Advance to the next slot, but stay at 5 once reached
    next_index = min(slots.index(selected) + 1, len(slots) - 1)
SystemExit