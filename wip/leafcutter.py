from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor
from pybricks.parameters import Icon, Port, Direction
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
Hub = PrimeHub()

left_arm= Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_arm = Motor(Port.F, Direction.COUNTERCLOCKWISE)
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
#lcolor_sensor = ColorSensor(Port.C)
#rcolor_sensor = ColorSensor(Port.D)
drive_base = DriveBase(left_motor, right_motor, 55,115)
drive_base.use_gyro(True)


drive_base.turn(-45)
drive_base.straight(620)
drive_base.turn(90)
drive_base.straight(110)
drive_base.turn(-20)
right_arm.run_angle(200, -90)