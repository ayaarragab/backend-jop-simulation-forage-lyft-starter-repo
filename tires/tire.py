from abc import abstractmethod
from servicable import Serviceable

class Tire(Serviceable):
    @abstractmethod
    def need_service(self):
        """
        will be implemented in the concrete classes
        """
        pass