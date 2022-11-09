from datetime import date

try:
    def promptAndExtractDate():
        print("Enter a Birthdate: ")
        month = int(input("Month(0 to Quit): "))
        if month == 0:
            return None
        else:
            day = int(input("Date: "))
            year = int(input("Year: "))
            return date(year, month, day)


    date1 = promptAndExtractDate()
    today = date.today()
    age = today.year - date1.year

    if age >= 21 :
        print("Is atleast 21 years of age: ", date1)
    else:
        print("Below 21 years of age: ", date1)

except:
    print("Not Eligible.")