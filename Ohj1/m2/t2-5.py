print("The program converts the talents, pounds, and lots to full kilograms and grams.")

talents = int(input("Enter the talents: "))
pounds = int(input("Enter the pounds: "))
lots = int(input("Enter the lots: "))

total_lots = talents * 20 * 32 + pounds * 32 + lots
total_grams = total_lots * 13.3
kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print(f"{kilograms} kilograms and {grams} grams")

input("Press Enter..")