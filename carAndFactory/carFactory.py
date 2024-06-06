from carAndFactory.car import Car
from datetime import date
"""
carFactory model
"""

class CarFactory:
    """
    carFactory class , applying factory design pattern
    """
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car("Calliope", current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car("Glissade", current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        return Car("Palindrome", current_date, last_service_date, warning_light_on=warning_light_on)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car("Rorschach", current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car("Thovex", current_date, last_service_date, current_mileage, last_service_mileage)