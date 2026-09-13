
from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor
from pybricks.parameters import Icon, Port, Direction, Stop
from pybricks.tools import wait
from pybricks.hubs import PrimeHub

Hub = PrimeHub()

arm = Motor(Port.D, Direction.COUNTERCLOCKWISE)
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
drive_base = DriveBase(left_motor, right_motor, 55,115)
drive_base.use_gyro(True) 

drive_base.settings(600, 600, 600,600)

drive_base.straight(370)

arm.run_target(100, 0)

drive_base.straight(-400)
#arm.run_target(100, -12)






