from prac_8.Car import Car
from random import randint


class UnreliableCar(Car):
    """An unreliable version of a car."""

    def __init__(self, car_name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(car_name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car, only sometimes, based on reliability."""
        random_number = randint(1, 100)
        distance_driven = 0
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven
