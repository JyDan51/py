import random 
while True:

    s = random.randint (1, 10)

    gg = int(input ("Gues the number: "))
    while gg != s:
    
        if gg > s:
            print ("NUMBER IS SMALLER!")
        
        else:
            print ("NUMBER IS BIGGEER!")
    
        gg = int(input ("Try again: "))

        
    print ("U got that! Number was",s )