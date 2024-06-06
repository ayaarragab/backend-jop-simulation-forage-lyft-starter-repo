from battery.nubbin import NubbinBattery
from battery.spindler import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tires.CarriganTires import CarriganTire
from tires.OctoprimeTires import OctoprimeTire
from car import CarParts

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tireWear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTire(tireWear)
        carParts = CarParts(engine=engine, battery=battery, tires=tires)
        car = Car(carParts)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tireWear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = OctoprimeTire(tireWear)
        carParts = CarParts(engine=engine, battery=battery, tires=tires)
        car = Car(carParts)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, tireWear):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTire(tireWear)
        carParts = CarParts(engine=engine, battery=battery, tires=tires)
        car = Car(carParts)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tireWear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTire(tireWear)
        carParts = CarParts(engine=engine, battery=battery, tires=tires)
        car = Car(carParts)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tireWear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = CarriganTire(tireWear)
        carParts = CarParts(engine=engine, battery=battery, tires=tires)
        car = Car(carParts)
        return car
