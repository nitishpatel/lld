from parking_spot import ParkingSpot
from vehicle import Vehicle
from typing import List

class Level:
    def __init__(self,floor:int,no_of_spots:int):
        self.floor = floor
        self.parking_spots: List[ParkingSpot] = [ParkingSpot(i) for i in range(no_of_spots)]

    def park_vehicle(self,vechile:Vehicle) -> bool:
        for spot in self.parking_spots:
            if spot.check_availability():
                spot.book_spot(vechile)
                return True

        return False

    def unpark_vechile(self,vechile:Vehicle) -> bool:
        for spot in self.parking_spots:
            if not spot.check_availability() and spot.get_parked_vehicle() == vechile:
                spot.unpark_vehicle()
                return True
        return False

    def display_availabile_spots(self)->None:
        print(f"Level {self.floor} Availbility:")
        for spot in self.parking_spots:
            print(f"Spot {spot.get_spot_number()} | {'Available' if spot.check_availability() else 'Booked'}")



