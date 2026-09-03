while True:
    input ("Hello")

    tries = 5 
    
    loggin = input ("Login: ")
    passw = input ("Password: ")
    
    while tries > 0:
        if loggin == "Python" and passw == "Rules":
            print ("Wellcome")
            break
        else:
            tries = tries - 1
            if tries > 0:
                print ("Wrong DATA, try again")
                loggin = input ("Login: ")
                passw = input ("Password: ")
    if tries == 0:
        print ("Wrong data BRUUUUUUH, try again later!")

    input ("Save the WORLD, my FINALE messege, goodBYE")