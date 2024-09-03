class Car:
    """Represents a car."""

    def _init_(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Displays car information."""
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

my_car = Car("Mercedez", "AMG", 2015)
my_car.display_info()