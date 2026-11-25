from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Color, Icon, Port, Direction, Stop
from pybricks.tools import wait, StopWatch
from pybricks.hubs import PrimeHub
# The speeds the robot starts with (same numbers as before).
DEFAULT_SETTINGS = (300, 900, 300, 900)
hub = PrimeHub()

left_arm = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_arm = Motor(Port.F, Direction.COUNTERCLOCKWISE)
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.CLOCKWISE)
lcolor_sensor = ColorSensor(Port.C)
rcolor_sensor = ColorSensor(Port.D)
drive_base = DriveBase(left_motor, right_motor, 55,115)
drive_base.use_gyro(True)
drive_base.settings(*DEFAULT_SETTINGS)


def breakpoint():
  # Wait for any button to be pressed, and save the result.
  pressed = []
  while not any(pressed):
      pressed = hub.buttons.pressed()
      wait(10)

  # Wait for all buttons to be released.
  while any(hub.buttons.pressed()):
      wait(10)

def start_run():
  # Call right before every menu option so every run starts the same way.
  # These are the same reset steps rr_es already uses. use_gyro(False)
  # also stops the drive base, so nothing is left holding from the last run.
  drive_base.use_gyro(False)
  wait(20)
  drive_base.reset()
  wait(20)
  drive_base.use_gyro(True)
  # Same speeds the robot has right after the program starts.
  drive_base.settings(*DEFAULT_SETTINGS)

def wait_for_gyro(max_wait_ms=3000):
  # If the gyro has not calibrated yet, turn the light red and wait
  # (up to 3 seconds) for it. Keep the robot still while it is red.
  # Most of the time the gyro is ready and this does not wait at all.
  if not hub.imu.ready():
      hub.light.on(Color.RED)
      timer = StopWatch()
      while not hub.imu.ready() and timer.time() < max_wait_ms:
          wait(10)
  hub.light.on(Color.GREEN)