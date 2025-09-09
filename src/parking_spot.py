from .util import Util
from .vehicle import Vehicle, VehicleSize

class ParkingSpot:
    spot_size: VehicleSize
    spot_id: str
    is_occupied: bool
    parked_vehicle: Vehicle | None

    def __init__(self, spot_size: VehicleSize) -> None:
        self.spot_size = spot_size
        self.spot_id = Util.generate_uuid()
        self.is_occupied = False
        self.parked_vehicle = None

    def get_id(self) -> str:
        return self.spot_id

    def can_fit_vehicle(self, vehicle: Vehicle) -> bool:
        return self.spot_size >= vehicle.size
    
    def is_available(self) -> bool:
        return not self.is_occupied
    
    def park_vehicle(self, vehicle: Vehicle) -> None:
        if not self.can_fit_vehicle(vehicle):
            raise Exception(f"Parking spot: {self.spot_id} of size: {self.spot_size} cannot fit vehicle: {vehicle} of size: {vehicle.size}")
        if not self.is_available():
            raise Exception(f"Parking spot: f{self.spot_id} is already occupied by: {self.parked_vehicle}")
        
        self.is_occupied = True
        self.parked_vehicle = vehicle

    def unpark_vehicle(self) -> None:
        if not self.is_occupied:
            raise Exception(f"Parking spot: f{self.spot_id} cannot unpark vehicle because there is no vehicle parked: {self.park_vehicle}")
        self.is_occupied = False
        self.parked_vehicle = None