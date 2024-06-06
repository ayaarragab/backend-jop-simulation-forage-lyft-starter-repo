"""
car model
"""
from servicable import Serviceable
class Car(Serviceable):
    def __init__(self, battery, engine):
        self.battery = battery
        self.engine = engine

    def needs_service(self):
        return self.battery.need_service() or self.engine.need_service()
