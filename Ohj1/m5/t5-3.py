num = int(input ("Enter number: "))

is_prime = True 

if num < 2:
    is_prime = False

else:
    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break

if is_prime: 
    print ("Prime number")

else:
    print ("Not prime number")