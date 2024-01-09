def absoulte_value():
    number = int(input("Enter the number: "))

    if number <= 0:
        print(f"The absolute value of {number} is = {-1 * number}")
    else:
        print(f"The absolute value of {number} is = {number}")    

if __name__ == "__main__":
    absoulte_value()   

"""Can be done using this too better use the complex number method 
def absoulut_value():
    number = int(input("Enter the number: "))
    return (value**2)**(0.5)
    
"""    