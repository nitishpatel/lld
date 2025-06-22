from level import Level
from typing import List
from vehicle import Vehicle

class ParkingLot:
    '''Parking Lot Class'''
    _instance = None
    def __init__(self):
        if ParkingLot._instance is not None:
            raise RuntimeError("This is a singleton class")
        else:
            ParkingLot._instance  = self
            self.levels: List[Level] = []

    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            return ParkingLot()
        return ParkingLot._instance

    def add_level(self,level:Level) -> None:
        self.levels.append(level)

    def park(self, vehicle: Vehicle)-> bool:
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False

    def unpark(self,vehicle:Vehicle) -> bool:
        for level in self.levels:
            if level.unpark_vechile(vehicle):
                return True
        return False

    def display_available_spots(self)-> None:
        for level in self.levels:
            level.display_availabile_spots()