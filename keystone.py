from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor
from pybricks.parameters import Icon, Port, Direction
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
from robot import drive_base, right_arm
def keystone_mission():
  drive_base.straight(350)
  right_arm.run_angle(200,-270)
  right_arm.run_angle(200,270)
  drive_base.straight(-350)



