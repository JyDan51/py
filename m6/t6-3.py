# 3.785

def literto (galons):
    return galons * 3.785

qgalons = float(input ("Enter galons: "))

while qgalons >= 0:
    liters = literto(qgalons)
    print ("Liters: ", liters)
    qgalons = float(input ("Enter galons: "))