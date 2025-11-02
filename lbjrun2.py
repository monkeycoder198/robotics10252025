from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
lbj=DriveBase(Motor(Port.F, Direction.COUNTERCLOCKWISE), Motor(Port.B), 56, 84)
lbj.use_gyro(True)

def run2():
   lbj.settings(700,350)
   lbj.straight(575)


   lbj.settings(200,100)
   lbj.straight(25)
   lbj.settings(970,970)


   #lbj.turn(-5)
   lbj.straight(-200)
   lbj.straight(-200)


   lbj.curve(550,-30)
   lbj.curve(550,30)
   lbj.straight(-550)

   '''
   lbj.turn(-90)
   lbj.straight(150)
   lbj.turn(90)
   lbj.straight(800)
   lbj.turn(90)
   lbj.straight(30)


   for _ in range(1,20):
       lbj.turn(-6)
       #lbj.settings(500,125)
       lbj.straight(-30)'''

run2()
