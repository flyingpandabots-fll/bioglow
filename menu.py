
import sys
from keystone import keystone_mission
from leafcutter_with_elder import leafcutter_mission
from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Icon, Port, Direction, Stop
from pybricks.tools import wait, hub_menu
from pybricks.hubs import PrimeHub
import robot
from drone import drone_mission
from rock import rock_mission
from rr_es import rr_es_mission
from vine import vine_mission
from leafcutter_with_elder import leafcutter_mission

#1 is drone mission, 2 is reaching roots and exploding seeds, 3 is  the rock misson , 4 is leafcutter with elder and window to the past , 5 is vine
hub = PrimeHub()
while True:
    #hub.light.on(Icon.HAPPY)
    selected = hub_menu("1", "2", "3", "4", "5", "6")
    if selected == "1":
        vine_mission()
    elif selected == "2":
        rock_mission()
    elif selected == "3":
        rr_es_mission()
    elif selected == "4":
        drone_mission()
    elif selected == "5":
        leafcutter_mission()
    elif selected == "6":
        keystone_mission()

SystemExit