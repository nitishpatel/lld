from vehicle_type import VehicleType
from vehicle import Vehicle

class ParkingSpot:
    def __init__(self,spot_number:int):
        self.parked_vechile = None
        self.spot_number = spot_number

    def check_availability(self):
        return self.parked_vechile is None

    def book_spot(self,vechile: Vehicle):
        if self.check_availability():
          self.parked_vechile = vechile
        else:
            raise ValueError("Spot Already Booked")

    def unpark_vehicle(self) -> None:
        self.parked_vechile = None

    def get_parked_vehicle(self) -> Vehicle:
        return self.parked_vechile

    def get_spot_number(self) -> int:
        return self.spot_number


