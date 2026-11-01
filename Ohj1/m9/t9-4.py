import random


class Car:
    def __init__ (self, number, max_speed):
        self.number = number
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate (self, change):
        self.speed = self.speed + change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0
    def drive (self, hours):
        self.distance = self.distance + self.speed * hours
cars = []

for i in range (1, 11):
    number = "ABC-" + str(i)
    max_speed = random.randint(100, 200)
    car = Car(number, max_speed)
    cars.append(car)
finished = False

while finished == False:
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)
        if car.distance > 10000:
            finished = True

print(f"{'Number':<10} {'Max km/h':<10} {'SpeeEd km/h':<12} {'Distance km':<12}")

for car in cars:
    print(f"{car.number:<10} {car.max_speed:<10} {car.speed:<12} {car.distance:<12}")