from abc import ABC, abstractmethod
from servicable import Serviceable
"""
battery interface module
"""
class Battery(ABC, Serviceable):
    @abstractmethod
    def need_service(self):
        """
        will be implemented in the concrete classes
        """
        pass