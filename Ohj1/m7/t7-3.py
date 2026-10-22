airoports = {}

while True:
    print ("1 - Add airoport")
    print ("2 - Find airoport")
    print ("3 - EXIT")

    choice = input ("Choose the action: ")

    if choice == "3":
        break

    elif choice == "1":
        code = input ("Enter ICAO code: ")
        name = input ("Enter airport name: ")
        airoports[code] = name
        print ("Airport saved")

    elif choice == "2":
        code = input ("Enter ICAO code: ")

        if code in airoports:
            print ("Airoport:", airoports[code])
        else:
            print ("404")