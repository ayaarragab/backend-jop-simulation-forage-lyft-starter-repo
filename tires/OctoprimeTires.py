from tires.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, array):
        self.array = array
    def need_service(self):
        return sum(self.array) >= 3