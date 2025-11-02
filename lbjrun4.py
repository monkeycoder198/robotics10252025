from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

lbj=DriveBase(Motor(Port.F, Direction.COUNTERCLOCKWISE), Motor(Port.B), 56, 84)
lbj.use_gyro(True)

lbj.settings(700,700,970,970)
lbj.straight(1045)
lbj.turn(80)

lbj.straight(135)
#Repeater Loop - Do the mission with the rope (Decent amount of points)
#We can only swivel it in one direction :(

for _ in range(1,16):
   lbj.turn(60)
   lbj.turn(-60)
   lbj.straight(-2)
lbj.straight(-120)
lbj.turn(-70)
lbj.straight(700)
