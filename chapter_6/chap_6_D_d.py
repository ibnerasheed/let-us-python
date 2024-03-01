def reverse(num):
    reverse = 0
    while num != 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse


def is_palindrome(num):
    return reverse(num)== num

def main():
    number = int(input("Enter the number: "))
    reverse_number = reverse(number)
    print(f"The reverse of the {number} is {reverse_number}")
    if reverse_number == number:
        print(f"{number} is palindrome.")
    else:
        print(f"{number} is not palindrome.")
            
      
if __name__ == "__main__":
    main()