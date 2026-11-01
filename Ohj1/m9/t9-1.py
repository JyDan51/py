class Car:
    def __init__ (self, number, max_speed):
        self.number = number
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0


car = Car ("ABC-123", 142)

print ("Registration number:", car.number)
print ("Maximum speed:", car.max_speed)
print ("Current speed:", car.speed)
print ("Travelled distance:", car.distance)