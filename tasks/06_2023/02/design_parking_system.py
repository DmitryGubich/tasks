class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.parking = {1: big, 2: medium, 3: small}

    def add_car(self, car_type: int) -> bool:
        if self.parking.get(car_type):
            self.parking[car_type] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
if __name__ == "__main__":
    parking_system = ParkingSystem(1, 1, 0)
    assert parking_system.add_car(1) is True
    assert parking_system.add_car(2) is True
    assert parking_system.add_car(3) is False
    assert parking_system.add_car(1) is False
