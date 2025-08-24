from typing import Optional
from parking_spot import ParkingSpot
from vehicle import Vehicle


class ParkingFloor:
    floor_number: int
    spots: dict[str, ParkingSpot]

    def __init__(self, floor_number: int) -> None:
        self.floor_number = floor_number
        spots = {}

    def add_spot(self, spot: ParkingSpot) -> None:
        self.spots[spot.get_id()] = spot

    def find_available(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
        for spot_id, spot in self.spots.items():
            if spot.is_available() and spot.can_fit_vehicle(vehicle):
                return spot
        
        return None

    def display_availability(self) -> None:
        for spot_id, spot in self.spots.items():
            if spot.is_available():
                print(f"{spot.spot_size}")