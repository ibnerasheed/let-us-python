def is_leap_year(year):
    divisor = 4
    if year % 100:
        divisor = 400
    return bool(year % divisor)


def main():
    year = int(input("Enter the year: "))

    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} isn't a leap year.")    

if __name__ == '__main__':
    main() 
