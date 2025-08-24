# from parking_strategy import ParkingStrategy
from parking_floor import ParkingFloor
from parking_ticket import ParkingTicket

class ParkingLotSystem:
    # parking_strategy: ParkingStrategy | None
    instance: "ParkingLotSystem"
    floors: list[ParkingFloor]
    active_tickets: dict[str, ParkingTicket]

    def __init__(self) -> None:
        # self.parking_strategy = None
        self.floors = []
        self.active_tickets = {}

    # singleton initialization
    def __new__(cls) -> "ParkingLotSystem":
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance