class Car:
    def __init__ (self, number, max_speed):
        self.number = number
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate (self, change):
        self.speed += change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0
    def drive(self, hours):
        self.distance += self.speed * hours


class ElectricCar (Car):
    def __init__(self, number, max_speed, battery_capacity):
        super().__init__(number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar (Car):
    def __init__(self, number, max_speed, tank_volume):
        super().__init__(number, max_speed)
        self.tank_volume = tank_volume


battery_bro = ElectricCar ("ABC-15", 180, 52.5)
thirsty_car = GasolineCar ("ACD-123", 165, 32.3)

battery_bro.accelerate (100)
thirsty_car.accelerate (80)

battery_bro.drive (3)
thirsty_car.drive (3)

print (battery_bro.number, battery_bro.distance, "km")
print (thirsty_car.number, thirsty_car.distance, "km")