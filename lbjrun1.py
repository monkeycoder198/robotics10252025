from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


hub = PrimeHub()
db=DriveBase(Motor(Port.F, Direction.COUNTERCLOCKWISE), Motor(Port.B, Direction.CLOCKWISE), 56, 84)
db.use_gyro(True)


db.settings(700,350)
db.straight(650)
db.straight(-150)
db.turn(30)
db.straight(210)
db.turn(-79)


db.settings(100,110)
db.straight(240)
db.straight(-200)

