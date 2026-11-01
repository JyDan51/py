class Car:
    def __init__(self, number, max_speed):
        self.number = number
        self.max_speed = max_speed
        self.speed = 0
        self.ditsance = 0

    def accelerate(self, change):
        self.speed = self.speed + change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0
    def drive(self, hours):
        self.ditsance = self.ditsance + self.speed * hours


car = Car ("ABC-123", 142)

car.ditsance = 2000
car.accelerate (60)
car.drive (1.5)

print ("Travelled ditsance:", car.ditsance)