from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Icon, Port, Direction, Stop
from pybricks.tools import wait
from pybricks.hubs import PrimeHub

Hub = PrimeHub()
#initialize motors and sensors
left_arm= Motor(Port.A, Direction.COUNTERCLOCKWISE, gears=[20,12,12,20])
right_arm = Motor(Port.F, Direction.COUNTERCLOCKWISE, gears=[20,12,12,20])
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
lcolor_sensor = ColorSensor(Port.C)
rcolor_sensor = ColorSensor(Port.D)
drive_base = DriveBase(left_motor, right_motor, 55,115)
drive_base.use_gyro(True)
drive_base.settings(900,900,900,900)


#go to the mission 5
drive_base.straight(780)
#solve the mission 5
right_arm.run_angle(600, -360)
#coming back
drive_base.straight(-630)
#going to mission 2
drive_base.turn(-45)
drive_base.straight(-147)
drive_base.turn(90)
right_arm.run_angle(600, -40)
#left arm down going to mission 2
left_arm.run_angle(100, -150)
drive_base.straight(230)
#solve mission 2
left_arm.run_angle(100,40)
drive_base.straight(-20)
left_arm.run_angle(100,15)
#drive_base.straight(-300)
drive_base.arc(-460,-50)



'''

#coming back


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
'''