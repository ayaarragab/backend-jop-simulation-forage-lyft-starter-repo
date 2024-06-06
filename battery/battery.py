from abc import abstractmethod
from servicable import Serviceable
"""
battery interface module
"""
class Battery(Serviceable):
    @abstractmethod
    def need_service(self):
        """
        will be implemented in the concrete classes
        """
        pass