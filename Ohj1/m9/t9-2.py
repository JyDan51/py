class Car:
    def __init__ (self, number, max_speed):
        self.number = number
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed = self.speed + change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0


car = Car ("ABC-123", 142)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print("Current speed:", car.speed)

car.accelerate(-200)
print ("Final speed:", car.speed)