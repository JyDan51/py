import random

def dice(sides):
    return random.randint(1, sides)

roll = 0

max = int(input ("How many sides? "))

while roll != max:
    roll = dice(max)
    print ("Roll is",roll)