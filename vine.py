from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Icon, Port, Direction, Stop
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
from robot import drive_base
def vine_mission():
    # Go to vine mission
    drive_base.turn(43)
    drive_base.straight(-640)
    drive_base.turn(-45)

    #Go slow and push vine down
    drive_base.settings(100, 100, 100, 100)
    drive_base.straight(-120)
    drive_base.straight(120)

    # Go back home
    drive_base.settings(900, 900, 900, 900)
    drive_base.turn(45)
    drive_base.straight(680)
    drive_base.stop()