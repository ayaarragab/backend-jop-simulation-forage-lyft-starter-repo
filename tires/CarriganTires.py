from tires.tire import Tire

class CarriganTire(Tire):
    def __init__(self, array):
        self.array = array
    def need_service(self):
        for num in self.array:
            if num >= 0.9:
                return True
        return False