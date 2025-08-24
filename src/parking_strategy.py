from abc import ABC, abstractmethod
from parking_spot import ParkingSpot
from parking_floor import ParkingFloor
from vehicle import Vehicle

class ParkingStrategy(ABC):
    @abstractmethod
    def find_spot(self, parking_floor: list[ParkingFloor], vehicle: Vehicle) -> ParkingSpot | None:
        pass

class DefaultStrategy(ParkingStrategy):
    def find_spot(self, parking_floor: list[ParkingFloor], vehicle: Vehicle) -> ParkingSpot | None:
        pass