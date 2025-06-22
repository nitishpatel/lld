from parking_lot import ParkingLot
from level import Level
from car import Car
from motorcycle import MotorCycle
from truck import Truck

if __name__ == "__main__":
    parking_lot = ParkingLot.get_instance()
    parking_lot.add_level(Level(1,100))
    parking_lot.add_level(Level(2,80))

    car = Car("ABC111")
    truck = Truck("ABC112")
    motorcycle = MotorCycle("ABC123")

    parking_lot.park(car)
    parking_lot.park(truck)
    parking_lot.park(motorcycle)

    parking_lot.display_available_spots()

    parking_lot.unpark(motorcycle)

    parking_lot.display_available_spots()