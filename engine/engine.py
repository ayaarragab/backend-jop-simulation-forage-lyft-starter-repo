from abc import ABC
from servicable import Serviceable
"""
engine interface module
"""
class Engine(ABC, Serviceable):
    def need_service(self):
        """
        will be implemented in the concrete classes
        """
        pass