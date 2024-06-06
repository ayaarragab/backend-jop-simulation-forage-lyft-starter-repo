from battery.battery import Battery
"""
spindler battery model
"""
import math
class SpindlerBattery(Battery):
    """
    SpindlerBattery class implements battery interface
    """
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    def need_service(self):
        return math.ceil((self.current_date - self.last_service_date).days/360) >= 3