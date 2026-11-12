
from keystone import keystone_mission
from leafcutter_with_elder import leafcutter_mission
from drone import drone_mission
from rock2 import rock_mission
from rr_es import rr_es_mission
from vine import vine_mission

from pybricks.tools import hub_menu
from pybricks.hubs import PrimeHub
from robot import drive_base,right_arm

hub = PrimeHub()

while True:
    selected = hub_menu("0", "1", "2", "3", "4", "5")
    if selected == "0":
        drive_base.straight(-100)
        right_arm.run_angle(200,-90)
    if selected == "1":
        rock_mission()
        vine_mission()

    elif selected == "2":
        rr_es_mission()

    elif selected == "3":
        drone_mission()

    elif selected == "4":
        leafcutter_run()

    elif selected == "5":
        keystone_mission()
SystemExit