from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


hub = PrimeHub()
db=DriveBase(Motor(Port.F, Direction.COUNTERCLOCKWISE), Motor(Port.B, Direction.CLOCKWISE), 56, 84)
db.use_gyro(True)


e=Motor(Port.E)


db.settings(700,350)
db.straight(650)
db.straight(-150)
db.turn(30)
db.straight(210)
db.turn(-79)


db.settings(100,110)
db.straight(240)
db.straight(-200)


db.settings(970,970)
db.turn(120)


e.run_angle(100, -50)
db.straight(225)


db.settings(300,970)
db.straight(74)
e.run_angle(100,100)
e.run_angle(90,90)
