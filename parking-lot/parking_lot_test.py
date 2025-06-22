import pytest
from parking_lot import ParkingLot
from level import Level
from car import Car
from truck import Truck
from motorcycle import MotorCycle


@pytest.fixture
def parking_lot():
    # Reset the singleton instance for isolated test runs
    ParkingLot._instance = None
    lot = ParkingLot.get_instance()
    lot.add_level(Level(1, 2))
    lot.add_level(Level(2, 3))
    return lot


def test_add_levels(parking_lot):
    assert len(parking_lot.levels) == 2
    assert parking_lot.levels[0].floor == 1
    assert parking_lot.levels[1].floor == 2


def test_park_vehicles(parking_lot):
    car = Car("CAR001")
    bike = MotorCycle("BIKE001")
    truck = Truck("TRUCK001")

    assert parking_lot.park(car) is True
    assert parking_lot.park(bike) is True
    assert parking_lot.park(truck) is True


def test_park_until_full(parking_lot):
    # Level 1 has 2, Level 2 has 3 = 5 total spots
    vehicles = [Car(f"CAR{i}") for i in range(5)]
    for v in vehicles:
        assert parking_lot.park(v) is True

    extra = Truck("EXTRA999")
    assert parking_lot.park(extra) is False  # No more space


def test_unpark_existing_vehicle(parking_lot):
    car = Car("TOREMOVE")
    parking_lot.park(car)
    assert parking_lot.unpark(car) is True


def test_unpark_nonexistent_vehicle(parking_lot):
    bike = MotorCycle("GHOST999")
    assert parking_lot.unpark(bike) is False


def test_display_available_spots(capsys, parking_lot):
    parking_lot.park(Car("A"))
    parking_lot.park(Truck("B"))

    parking_lot.display_available_spots()

    captured = capsys.readouterr()
    assert "Level 1 Availbility:" in captured.out
    assert "Available" in captured.out or "Booked" in captured.out
