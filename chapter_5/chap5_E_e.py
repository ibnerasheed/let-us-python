def absolute_number(number):
    if number <= 0:
        return -1*number
    else:
        return number


def main():
    number = int(input("Enter the number: "))
    result = absolute_number(number)

    if number <= 0:
        print(f"The absolute value of {number} is = {result}")
    else:
        print(f"The absolute value of {number} is = {result}")    

if __name__ == "__main__":
    main()   

"""Can be done using this too better use the complex number method 
def absoulut_value():
    number = int(input("Enter the number: "))
    return (value**2)**(0.5)
    
"""    