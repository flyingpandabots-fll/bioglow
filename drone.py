from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Icon, Port, Direction, Stop
from pybricks.tools import wait
from pybricks.hubs import PrimeHub


Hub = PrimeHub()

def breakpoint():
  # Wait for any button to be pressed, and save the result.
  pressed = []
  while not any(pressed):
      pressed = Hub.buttons.pressed()
      wait(10)

  # Wait for all buttons to be released.
  while any(Hub.buttons.pressed()):
      wait(10)
#initialize motors and sensors
left_arm= Motor(Port.A, Direction.COUNTERCLOCKWISE, gears=[20,12,12,20])
right_arm = Motor(Port.F, Direction.COUNTERCLOCKWISE, gears=[20,12,12,20])
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
lcolor_sensor = ColorSensor(Port.C)
rcolor_sensor = ColorSensor(Port.D)
drive_base = DriveBase(left_motor, right_motor, 55,115)
drive_base.use_gyro(True)
drive_base.settings(450,450,450,450)
#driving to mission 1 and pushing drone
drive_base.straight(620)
drive_base.straight(-50)
# getting alighned with the landing area
drive_base.turn(-30)
drive_base.straight(55)
drive_base.straight(-35)
drive_base.turn(-35)
#solving the drone mission
drive_base.turn(65)
#going home
drive_base.straight(-150)
left_arm.run_angle(200,-200)
drive_base.turn(-45)
#breakpoint()
drive_base.straight(280)
#breakpoint()
drive_base.turn(20)
#breakpoint()
drive_base.straight(20)
#drive_base.turn(-10)
left_arm.run_angle(100, 100)
#breakpoint()
drive_base.straight(50)
#breakpoint()
left_arm.run_angle(200, -100)
#breakpoint()
drive_base.turn(45)
drive_base.straight(800)
drive_base.stop()