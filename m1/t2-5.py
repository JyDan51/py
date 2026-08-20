import math
print ("The program converts the talents, pounds, and lots to full kilograms and grams and outputs the result to the user")

talents = input("Enter the talents: ")
pounds = input("Enter the pounds: ")
lots = input("Enter the lots: ")

resultT = talents * 0.03333
resultP = resultT * 0.45359237
resultL = resultP * 0.01667

print(f"talents to kg: {resultT}")
print(f"pounds to kg: {resultP}")
print(f"lots to kg: {resultL}")

input("Press Enter..")