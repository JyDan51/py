input ("Hello")

n = input ("Numbers pls: ")

if n != "":
    number = float(n)
    
    sml = number
    lrg = number
    
    n = input ("Numbers pls: ")

while n != "":
    number = float(n)
    
    if number < sml:
        sml = number
        
    if number > lrg:
        lrg = number
        
    n = input ("Numbers pls: ")
    
print ("Smallest: ", sml)
print ("Largest: ", lrg)

input ("Save the world, my finale messege, goodbye")