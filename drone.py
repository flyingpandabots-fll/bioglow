from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Color, Icon, Port, Direction, Stop
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
import robot




#initialize motors and sensors
def drone_mission():
    robot.drive_base.settings(450,450,450,450)
    #driving to mission 1 and pushing drone
    robot.drive_base.straight(620)
    robot.drive_base.straight(-50)
    # getting alighned with the landing area
    robot.drive_base.turn(-30)
    robot.drive_base.straight(55)
    robot.drive_base.straight(-35)
    robot.drive_base.turn(-35)
    #solving the drone mission
    robot.drive_base.turn(65)
    robot.drive_base.straight(-150)
    robot.left_arm.run_angle(200,-150)
    robot.drive_base.turn(-45)
    #breakpoint()
    #going to the biocentic arcitecture
    #alighn with black
    robot.drive_base.drive(150, 0)
    while robot.rcolor_sensor.reflection() > 15:
        print(robot.rcolor_sensor.reflection())
    robot.drive_base.stop()
    #alighning to the biocentric architecture
    robot.drive_base.turn(22)
    robot.drive_base.straight(20)
    robot.drive_base.turn(-5)
    #solving the bird part 
    robot.left_arm.run_angle(20, 55)
    robot.drive_base.turn(5)
    #solving the compost hatch
    robot.left_arm.run_angle(100, -20)
    robot.drive_base.straight(50)
    robot.left_arm.run_angle(200, -50)
    #driving to home
    robot.drive_base.turn(40)
    robot.drive_base.straight(800)
    robot.drive_base.stop()