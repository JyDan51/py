input ("Hello")

s = input("Sex: ").strip().upper()
hb = float(input("hemoglobin: "))

if s == "F":
    if hb <117:
        print ("Low")
    elif 117 <= hb <= 175:
        print ("Normal")
    else:
        print ("High")
    
elif s == "M":
    if hb <134:
        print ("Low")
    elif 134 <= hb <= 195:
        print ("Normal")
    else:
        print ("High")
    
else:
    print("Try again")

input ("Press Enter..")