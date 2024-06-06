from abc import ABC, abstractmethod
"""
engine interface module
"""
class Engine(ABC):
    @abstractmethod
    def need_service(self):
        """
        will be implemented in the concrete classes
        """
        pass