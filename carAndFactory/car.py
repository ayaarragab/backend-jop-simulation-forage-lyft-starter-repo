"""
car model
"""
from servicable import Serviceable
from carAndFactory.carParts import CarParts
class Car(Serviceable):
    def __init__(self, carParts):
        self.carParts = carParts

    def needs_service(self):
        return self.battery.need_service() or self.engine.need_service()
