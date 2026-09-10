seasons = (
    "Talvi", "talvi", "kevat",
    "kevat", "kevät", "kesä",
    "kesä", "Kesä", "syksy", 
    "Syksy", "syksy", "talvi"
)

month = int(input ("What is the month number? "))

if 1 <= month <= 12:
    print (seasons[month - 1])
else:
    print ("Wrong number")