from abc import ABC
from enum import IntEnum

class VehicleSize(IntEnum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Vehicle(ABC):
    size: VehicleSize
    license_number: str

    def __init__(self, size: VehicleSize, license_number: str):
        if size == None:
            raise Exception("Vehicle size must be specified")
        if (license_number == None or license_number == ""):
            raise Exception("License no must be specified")
        
        self.size = size
        self.license_number = license_number

class Car(Vehicle):
    def __init__(self, license_number: str):
        super().__init__(VehicleSize.MEDIUM, license_number)

class Truck(Vehicle):
    def __init__(self, license_number: str):
        super().__init__(VehicleSize.LARGE, license_number)

class Motorcycle(Vehicle):
    def __init__(self, license_number: str):
        super().__init__(VehicleSize.SMALL, license_number)