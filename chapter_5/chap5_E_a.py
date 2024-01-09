def odd_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def main():
    number = int(input("Please enter the number: "))
    if odd_even(number):
        print(f"The {number} is even")
    else:
        print(f"the {number} is odd")
    

if __name__ == "__main__":
    main()