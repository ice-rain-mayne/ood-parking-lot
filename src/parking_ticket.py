from encodings import undefined
from parking_spot import ParkingSpot
from vehicle import Vehicle
from util import Util

class ParkingTicket:
    spot: ParkingSpot
    ticketId: str
    entry_timestamp: int
    exit_timestamp: int | None
    vehicle: Vehicle

    def __init__(self, vehicle: Vehicle, spot: ParkingSpot, entry_timestamp: int) -> None:
        self.spot = spot
        self.ticketId = Util.generate_uuid()
        self.entry_timestamp = entry_timestamp
        self.exit_timestamp = None
        self.vehicle = vehicle