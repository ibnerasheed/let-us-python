def main():
    a = 4
    b = 3
    print(f"Before swap: a = {a}, b = {b}")
    a = a ^ b #a = a + b
    b = b ^ a #b = a - b
    a = a ^ b #a = a - b
    print(f"After swap: a = {a}, b = {b}")

if __name__ == "__main__":
    main()