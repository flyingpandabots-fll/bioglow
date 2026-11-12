from pybricks.robotics import DriveBase
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.parameters import Color, Icon, Port, Direction
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
from robot import drive_base, right_arm, hub


def leafcutter_run():
    drive_base.settings(300, 900, 300, 900)
    right_arm.run_angle(200,-120)
    
    # Code to go to the mission "Leafcutter Frenzy"
    drive_base.straight(80)
    drive_base.turn(-45)
    drive_base.straight(620)
    
    # Turn to face the leafcutter
    drive_base.turn(90)
    
    #Put arm down
    right_arm.run_angle(200,120)
    
    #Change to slow speed
    drive_base.settings(100, 100, 100, 100)
    
    # Solve leafcutter
    drive_base.straight(120)
    drive_base.straight(-20)
    right_arm.run_angle(200, -25)

    # Go back to fast speed
    drive_base.settings(300, 900, 300, 900)
    drive_base.turn(-42)
    drive_base.straight(20)
    
    # Solve humungous fungus
    right_arm.run_angle(200, -110)
    
    # Go to and solve window to the past
    drive_base.arc(300, -45)

    # Go to forest elder
    drive_base.turn(-70)

    drive_base.straight(-260)

    # Solve forest elder
    drive_base.turn(40)

    # Go back home
    drive_base.arc(-90, 120)
    drive_base.straight(500)
    drive_base.stop()

    
