from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor
from pybricks.parameters import Icon, Port, Direction, Stop
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
from robot import drive_base, right_arm
def keystone_mission():
  drive_base.use_gyro(True)
  drive_base.straight(350)
  right_arm.run_angle(200,-120)
  drive_base.turn(15)
  right_arm.run_angle(200,-240)

  drive_base.turn(-15)

  right_arm.run_angle(200,180)
  
  #drive_base.straight(-350)
  drive_base.stop()
