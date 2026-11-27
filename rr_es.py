from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Color, Icon, Port, Direction, Stop
from pybricks.tools import StopWatch, wait
from pybricks.hubs import PrimeHub
from robot import drive_base, right_arm, left_arm, hub

def rr_es_mission():
    drive_base.use_gyro(False)
    wait(20)
    drive_base.reset()
    wait(20)

    drive_base.use_gyro(True)
    drive_base.settings(300,900,300,900)
    right_arm.reset_angle(0)
    #go to the mission 5
    drive_base.straight(780)

    #solve the mission 5
    right_arm.run_angle(600, -400)
    drive_base.straight(-70)
    drive_base.straight(60)
    right_arm.run_angle(600, -600)
    #coming back
    hub_name = hub.system.info()["name"]
    print("Hub name:", hub_name)
    if hub_name == "Vedika's Hub": #Bingo
        drive_base.straight(-625)
    else: #Bluey!!
        drive_base.straight(-635)
    #going to mission 2
    drive_base.turn(-45)
    drive_base.straight(-165)
    drive_base.turn(90)
    #left arm down going to mission 2
    left_arm.run_angle(100, -140)
    #resetting right arm

    hub_name = hub.system.info()["name"]
    if hub_name == "Bingo":
        drive_base.straight(247)
    else:
        drive_base.straight(252)


    #solve mission 2
    left_arm.run_angle(100, 55, then=Stop.HOLD)
    #coming home
    drive_base.straight(50)  
    drive_base.straight(-50)   
    drive_base.arc(-460,-55)
    drive_base.stop()
    left_arm.run_angle(100, 90)