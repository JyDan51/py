import random

class Car:
    def __init__(self, number, max_speed):
        self.number = number
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate (self, change):
        self.speed += change


        if self.speed > self.max_speed:
            self.speed = self.max_speed
        elif self.speed < 0:
            self.speed = 0

    def drive (self, hours):
        self.distance += self.speed * hours
 
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes (self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status (self):
        print ("Car", "Max", "Speed", "Km", sep="\t")
        for car in self.cars:
            print (car.number, car.max_speed, car.speed, car.distance, sep="\t")

    def race_finished (self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True

cars = []
for i in range(1, 11):
    number = "ABC-" + str(i)
    max_speed = random.randint(100, 200)
    cars.append (Car(number, max_speed))

chaos_race = Race("Grand Demolition Derby", 8000, cars)
print (chaos_race.name)

hours = 0
while not chaos_race.race_finished():
    chaos_race.hour_passes()
    hours += 1

    if hours % 10 == 0:
        print ("Hour:", hours)
        chaos_race.print_status()

print ("Race finished after", hours, "hours")
chaos_race.print_status()