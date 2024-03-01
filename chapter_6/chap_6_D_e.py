def factorial(num):
    if num < 0:
        raise ValueError("Negative number")
    elif num == 0:
        print("The factorial of 0 is 1")
        return f"factorial is 1."
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial = factorial * i
        return f"the result is : {factorial}"   

factorial(2)