from abc import ABC, abstractmethod
"""
battery interface module
"""
class Battery(ABC):
    @abstractmethod
    def need_service(self):
        """
        will be implemented in the concrete classes
        """
        pass