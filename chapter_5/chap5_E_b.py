def leap_year():
    year = int(input("Enter the year: "))

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} isn't a leap year.")    

if __name__ == '__main__':
    leap_year()        