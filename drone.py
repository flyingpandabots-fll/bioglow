from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Color, Icon, Port, Direction, Stop
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
import robot


# Define target reflection threshold for black (e.g., < 20 or < 30)


BLACK_THRESHOLD = 15

def line_square(speed=100):
  # Start both motors moving forward


  robot.left_motor.run(speed)
  robot.right_motor.run(speed)


  left_hit = False
  right_hit = False
  # Loop until both sensors detect the line

  while not (left_hit and right_hit):
    if not left_hit and robot.lcolor_sensor.reflection() < BLACK_THRESHOLD:
      left_motor.hold()  # Stop/hold the left motor
      left_hit = True

    if not right_hit and robot.rcolor_sensor.reflection() < BLACK_THRESHOLD:
      robot.right_motor.hold()  # Stop/hold the right motor
      right_hit = True

  # Brief pause to settle
  wait(50)

#initialize motors and sensors
def drone_mission():
    robot.drive_base.settings(450,450,450,450)
    #driving to mission 1 and pushing drone
    robot.drive_base.straight(620)
    robot.drive_base.straight(-50)
    # getting aligned with the landing area
    robot.drive_base.turn(-30)
    robot.drive_base.straight(55)
    robot.drive_base.straight(-35)
    robot.drive_base.turn(-35)
    #solving the drone mission
    robot.drive_base.turn(50)
    
    robot.drive_base.straight(-20)
    robot.drive_base.turn(-55)
    robot.drive_base.turn(70)
    robot.drive_base.straight(-120)
    robot.drive_base.turn(-43)
    robot.drive_base.straight(400)
    robot.drive_base.straight(-40)
        
    robot.drive_base.turn(60)
        
    robot.drive_base.straight(800)
        
    robot.drive_base.stop()
drone_mission()