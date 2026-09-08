import random

dices = int ( input ("How many dice? "))
totald = 0

for i in range(dices):
    roll = random.randint(1,6)
    totald = totald + roll
    print ("So dices is ",roll)

print ("Total:", totald)