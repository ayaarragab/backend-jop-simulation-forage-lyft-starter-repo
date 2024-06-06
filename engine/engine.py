from abc import abstractmethod
from servicable import Serviceable
"""
engine interface module
"""
class Engine(Serviceable):
    @abstractmethod
    def need_service(self):
        """
        will be implemented in the concrete classes
        """
        pass