year = int(input("Gime year: "))

if year % 400 == 0:
    print ("Good")

elif year % 100 == 0:
    print ("No")

elif year % 4 == 0:
    print ("Good")

else:
    print ("No")
