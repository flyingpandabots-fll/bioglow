
import sys
from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Icon, Port, Direction, Stop
from pybricks.tools import wait, hub_menu
from pybricks.hubs import PrimeHub

#1 is drone mission, 2 is reaching roots and exploding seeds, 3 is  the rock misson , 4 is leafcutter with elder and window to the past , 5 is vine
hub = PrimeHub()
while True:
    #hub.light.on(Icon.HAPPY)
    selected = hub_menu("1", "2", "3", "4", "5")
    if selected == "1":
        
        import drone
    elif selected == "2":
        import rr_es
    elif selected == "3":
        import rock
    elif selected == "4":
        import leafcutter_with_elder
    elif selected == "5":
        import vine2

    SystemExit