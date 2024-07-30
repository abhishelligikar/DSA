year = int(input("Enter year to check for leap year : "))

print(year, "is a leap year" if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else "is not a leap year")

def check_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(f"{year} is a leap year" if check_leap(year) else f"{year} is not a leap year")

