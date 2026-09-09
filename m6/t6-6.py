import math

def priceunit (diameter, price):
    radius = diameter / 2 / 100
    area = math.pi * radius ** 2
    return price / area

diameter1 = float(input ("Pizza 1 diameter cm:"))
price1 = float(input ("Pizza 1 price euro:"))

firts = priceunit(diameter1, price1)

diameter2 = float(input ("Pizza 2 diameter cm:"))
price2 = float(input ("Pizza 2 price euro:"))

second = priceunit(diameter2, price2)

if firts < second:
    print("Pizza 1 is better!")

elif firts > second:
    print ("Pizza 2 is better")

else:
    print ("Both? both, Both Pizza is good")