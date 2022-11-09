from datetime import date

bornBefore = date(2000, 1, 24)

def promptAndExtractDate():
    print("Enter a Birthdate: ")
    month = int(input("Month(0 to Quit): "))
    if month == 0 :
        return None
    else:
        day = int(input("Date: "))
        year = int(input("Year: "))
        return date(year, month, day)

date1 = promptAndExtractDate()

while (date1):
    if date1 <= bornBefore:
        print("Is atleast 21 years of age: ", date1)
        break
    else:
        print("Below 21 years of age: ", date1)
        break