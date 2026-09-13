from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Icon, Port, Direction, Stop
from pybricks.tools import wait
from pybricks.hubs import PrimeHub

Hub = PrimeHub()

left_arm= Motor(Port.A, Direction.COUNTERCLOCKWISE, gears=[20,36])
right_arm = Motor(Port.F, Direction.COUNTERCLOCKWISE, gears=[20,36])
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
lcolor_sensor = ColorSensor(Port.C)
rcolor_sensor = ColorSensor(Port.D)
drive_base = DriveBase(left_motor, right_motor, 55,115)
drive_base.use_gyro(True)


left_arm.reset_angle(0)
drive_base.turn(30)
#left_arm.run_angle(500, -60)
left_arm.run_angle(500, 60)
#left_arm.run_angle(500, -120)
