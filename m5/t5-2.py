num = []

text = input("Entr the number pls: ")

while text != "":
    number = int(text)
    num.append(number)
    text = input("entr the number pls: ")

num.sort (reverse=True) 
print(num[:5])