from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Icon, Port, Direction, Stop
from pybricks.tools import wait
from pybricks.hubs import PrimeHub

Hub = PrimeHub()

left_arm= Motor(Port.A, Direction.COUNTERCLOCKWISE, gears=[20,12,12,20])
right_arm = Motor(Port.F, Direction.COUNTERCLOCKWISE, gears=[20,12,12,20])
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
lcolor_sensor = ColorSensor(Port.C)
rcolor_sensor = ColorSensor(Port.D)
drive_base = DriveBase(left_motor, right_motor, 55,115)
drive_base.use_gyro(True)
drive_base.settings(900,900,900,900)

#display smiley face
Hub.display.icon(Icon.HAPPY,)


drive_base.straight(780)
right_arm.run_angle(600, -360)
drive_base.straight(-760)

#drive_base.turn(45)
drive_base.arc()
right_arm.run_angle(900, 180)
left_arm.run_angle(100, -150)


drive_base.straight(300)
left_arm.run_angle(150, 50)

drive_base.straight(-50)
left_arm.run_angle(150, 30)
drive_base.straight(-250)

#drive_base.straight(-400)
#left_arm.run_target(100, -12)
Hub.display.icon(Icon.ARROW_UP,)