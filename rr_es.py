from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Color, Icon, Port, Direction, Stop
from pybricks.tools import StopWatch, wait
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
drive_base.use_gyro(False)
wait(20)
drive_base.reset()
wait(20)

drive_base.use_gyro(True)
drive_base.settings(300,900,300,900)

#print(rcolor_sensor.color())
#breakpoint()
#go to the mission 5
drive_base.straight(780)

#solve the mission 5
right_arm.run_angle(600, -400)
Hub.light.on(Color.RED)
drive_base.straight(-70)
Hub.light.on(Color.ORANGE)
drive_base.straight(40)
Hub.light.on(Color.YELLOW)
right_arm.run_angle(600, -400)
Hub.light.on(Color.GREEN)
#coming back
drive_base.straight(-600)
Hub.light.on(Color.BLUE)
#going to mission 2
drive_base.turn(-45)
Hub.light.on(Color.CYAN)
drive_base.straight(-147)
Hub.light.on(Color.MAGENTA)
drive_base.turn(90)
Hub.light.on(Color.RED)
right_arm.run_angle(600, 100)
Hub.light.on(Color.ORANGE)
#left arm down going to mission 2
left_arm.run_angle(100, -140)
Hub.light.on(Color.YELLOW)
drive_base.straight(240)
Hub.light.on(Color.GREEN)
#solve mission 2
left_arm.run_angle(100,45, then=Stop.HOLD)
#coming home
drive_base.arc(-460,-55)