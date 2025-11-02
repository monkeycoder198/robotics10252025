from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


hub = PrimeHub()


lbj=DriveBase(Motor(Port.F, Direction.COUNTERCLOCKWISE), Motor(Port.B), 56, 84)
lbj.use_gyro(True)


#Go Straight
lbj.settings(970,970)
lbj.straight(1500)
