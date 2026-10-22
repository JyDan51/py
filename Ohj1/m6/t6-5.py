def spnumbers  (numbers):
    result = []

    for number in numbers:
        if number % 2 == 0:
            result.append (number)

    return result

values = []

qtext = input ("Numbesr pls:")

while qtext != "":
    number = int(qtext)
    values.append(number)
    qtext = input ("Numbesr pls:")

filtered = spnumbers (values)
print ("Original;",values)
print ("Filtered:",filtered)