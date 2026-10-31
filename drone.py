from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Color, Icon, Port, Direction, Stop
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
drive_base.straight(-150)
left_arm.run_angle(200,-150)
drive_base.turn(-45)
#breakpoint()
#going to the biocentic arcitecture
#alighn with black
drive_base.drive(150, 0)
while rcolor_sensor.reflection() > 15:
    print(rcolor_sensor.reflection())
drive_base.stop()
#alighning to the biocentric architecture
drive_base.turn(22)
drive_base.straight(20)
drive_base.turn(-5)
#solving the bird part 
left_arm.run_angle(20, 55)
drive_base.turn(5)
#solving the compost hatch
left_arm.run_angle(100, -20)
drive_base.straight(50)
left_arm.run_angle(200, -50)
#driving to home
drive_base.turn(40)
drive_base.straight(800)
drive_base.stop()