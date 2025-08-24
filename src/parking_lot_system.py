from parking_strategy import ParkingStrategy
from parking_floor import ParkingFloor
from parking_ticket import ParkingTicket

class ParkingLotSystem:
    parking_strategy: ParkingStrategy
    instance: "ParkingLotSystem"
    floors: list[ParkingFloor]
    active_tickets: dict[str, ParkingTicket]

    def __init__(self) -> None:
        pass