class Car:

    wheel_number = 4

    def __init__(self, color, brand, year):
        self.color = color
        self.brand = brand
        self.year = year

    def description(self):
        return f"{self.year} {self.color} {self.brand}"
    
    def move(self):
        print(f"The {self.color} {self.brand} is moving.")

    def stop(self):
        print(f"The {self.color} {self.brand} has stopped.")

car1 = Car("red", "Toyota", 2020)
car2 = Car("blue", "Honda", 2018)

car2.wheel_number = 16

print(car1.move())
print(f"The total wheel number of car 2 is: {car2.wheel_number}")

print(car1.description())
    