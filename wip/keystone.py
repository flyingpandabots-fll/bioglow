from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor
from pybricks.parameters import Icon, Port, Direction
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
Hub = PrimeHub()

# Set up
armleft = Motor(Port.A, Direction.COUNTERCLOCKWISE)
armleft.run_target(200, 120)

Hub.display.icon(Icon.HAPPY,)
wait(2000)
