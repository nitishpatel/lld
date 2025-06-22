from vehicle_type import VehicleType
from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, vehicle_no:str):
        super().__init__(vehicle_no, VehicleType.CAR)
