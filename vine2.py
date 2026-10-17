from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Icon, Port, Direction, Stop
from pybricks.tools import wait
from pybricks.hubs import PrimeHub

hub = PrimeHub()
# Defines "Breakpoint"
def breakpoint():
  # Wait for any button to be pressed, and save the result.
  pressed = []
  while not any(pressed):
      pressed = hub.buttons.pressed()
      wait(10)

  # Wait for all buttons to be released.
  while any(hub.buttons.pressed()):
      wait(10)

left_arm= Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_arm = Motor(Port.F, Direction.COUNTERCLOCKWISE)
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
lcolor_sensor = ColorSensor(Port.C)
rcolor_sensor = ColorSensor(Port.D)
drive_base = DriveBase(left_motor, right_motor, 55,115)
drive_base.use_gyro(True)
drive_base.settings(300, 900, 300, 900)

# Go to vine mission
drive_base.turn(43)
drive_base.straight(-640)
drive_base.turn(-45)

#Go slow and push vine down
drive_base.settings(100, 100, 100, 100)
drive_base.straight(-120)
drive_base.straight(120)

# Go back home
drive_base.settings(900, 900, 900, 900)
drive_base.turn(45)
drive_base.straight(680)
drive_base.stop()