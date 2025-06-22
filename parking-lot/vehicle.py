from abc import ABC
from vehicle_type import VehicleType
class Vehicle(ABC):
    def __init__(self,vehicle_no:str, vehicle_type: VehicleType):
        self.vehicle_no = vehicle_no
        self.vehicle_type = vehicle_type

    def get_type(self):
        return self.vehicle_type