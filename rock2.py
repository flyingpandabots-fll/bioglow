
from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Icon, Port, Direction, Stop
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
from robot import drive_base, breakpoint

def rock_mission():
  drive_base.straight(-210)
  # Positions the robot to the starting position for the rock mission
  drive_base.turn(-11.5)
  drive_base.settings(200, 900, 200, 900)
  # Does the rock mission
  drive_base.straight(-190)
  drive_base.straight(200)
  drive_base.turn(-5)
  drive_base.straight(-210)
  drive_base.straight(180)
  drive_base.settings(900, 900, 900, 900)
      
  #drive_base.turn(9)
  #drive_base.straight(100)
  drive_base.stop()
  
