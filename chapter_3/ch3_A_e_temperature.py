def main():
    temp_f = int(input("Enter the value to convert into Celcius: "))
    temp_c = (temp_f - 32)*(5/9)
    print(f"The value of temperature in celcius is : {round(temp_c,3)}")


if __name__ == "__main__":
    main()