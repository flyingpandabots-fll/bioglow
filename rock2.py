
from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Icon, Port, Direction, Stop
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
from robot import drive_base, breakpoint

def rock_mission():
  drive_base.straight(-210)
  # Positions the robot to the starting position for the rock mission
  drive_base.turn(-9)

  drive_base.settings(200,200,200,200)
  # Does the rock mission
  drive_base.straight(-220)
  drive_base.straight(205)
  drive_base.settings(900, 900, 900, 900)
      
  #drive_base.turn(9)
  #drive_base.straight(100)
  drive_base.stop()
  
