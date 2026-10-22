names = set()

name = input ("Enter the name (Enter to stop): ")

while name !="":

    if name in names:
        print ("Already known")

    else:
        print ("New name")
        names.add(name)

    name = input("Enter a name (Enter to stop): ")

for name in names:
    print (name)