def totallist (numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total

values = [1, 2, 3, 4]
rusult = totallist(values)

print ("Total: ", rusult)