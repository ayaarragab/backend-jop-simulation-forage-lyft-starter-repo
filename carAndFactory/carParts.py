from battery import *
from engine import *
from tires import *

class CarParts:
    def __init__(self, battery=None, engine=None, tires=None):
        self.battery = battery
        self.engine = engine
        self.tires = tires