from pybricks.robotics import DriveBase
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.parameters import Color, Icon, Port, Direction
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
hub = PrimeHub()

def breakpoint():
  # Wait for any button to be pressed, and save the result.
  pressed = []
  while not any(pressed):
      pressed = hub.buttons.pressed()
      wait(10)

  # Wait for all buttons to be released.
  while any(hub.buttons.pressed()):
      wait(10)

# Initialize the Robot
left_arm= Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_arm = Motor(Port.F, Direction.COUNTERCLOCKWISE)
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
lcolor_sensor = ColorSensor(Port.C)
rcolor_sensor = ColorSensor(Port.D)
drive_base = DriveBase(left_motor, right_motor, 55,115)
drive_base.use_gyro(True)
drive_base.settings(300, 900, 300, 900)


right_arm.run_angle(200,-120)
# Code to go to the mission "Leafcutter Frenzy"
drive_base.straight(50)
drive_base.turn(-45)
drive_base.straight(620)
# Turn to face the leafcutter
drive_base.turn(90)

#Put arm down
right_arm.run_angle(200,120)

#Change to slow speed
drive_base.settings(100, 100, 100, 100)

# Solve leafcutter
drive_base.straight(110)

drive_base.straight(-20)


right_arm.run_angle(200, -25)

# Go back to fast speed
drive_base.settings(300, 900, 300, 900)
hub.light.on(Color.YELLOW)

drive_base.turn(-42)
hub.light.on(Color.GREEN)

drive_base.straight(-10)
hub.light.on(Color.BLUE)

# Solve humungous fungus
right_arm.run_angle(200, -110)
hub.light.on(Color.VIOLET)

# Go to and solve window to the past
drive_base.arc(300, -45)
hub.light.on(Color.GREEN)

# Go to forest elder
drive_base.turn(-80)
hub.light.on(Color.CYAN)

drive_base.straight(-230)
hub.light.on(Color.VIOLET)

# Solve forest elder
drive_base.turn(45)
hub.light.on(Color.CYAN)

# Go back home
drive_base.arc(-90, 120)
drive_base.straight(500)