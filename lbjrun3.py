from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
db=DriveBase(Motor(Port.F, Direction.COUNTERCLOCKWISE), Motor(Port.B, Direction.CLOCKWISE), 56, 84)

#Mission 6 - Run 3 - Dest. 1 
'''db.settings(970,970)
db.straight(745)
db.turn(-6)
db.settings(50,50)
db.straight(15)
db.settings(970,970)
db.straight(-215)'''

db.use_gyro(True)
db.settings(500, 425)
db.straight(720)
db.turn(-15)
db.straight(30)
db.straight(-25)
db.turn(15)
db.straight(-200)

db.turn(-16.5)
db.straight(263)
db.settings(700, None, 400, 600)
db.turn(-75)

db.straight(250)
db.turn(35)
db.straight(-1000)