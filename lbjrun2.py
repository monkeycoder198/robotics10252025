from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

lbj=DriveBase(Motor(Port.F, Direction.COUNTERCLOCKWISE), Motor(Port.B), 56, 84)
lbj.use_gyro(True)


lbj.settings(500,225,970,970)
lbj.straight(800)
lbj.turn(35)


lbj.straight(160)
#Repeater Loop - Do the mission with the rope (Decent amount of points)
#We can only swivel it in one direction :(


for _ in range(1,18):
   lbj.turn(50)
   lbj.turn(-50)


lbj.straight(-180)
lbj.turn(-30)
lbj.straight(-200)
lbj.turn(-20)
lbj.straight(-600)
