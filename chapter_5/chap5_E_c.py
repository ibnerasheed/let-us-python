def ages():
    ram_age = int(input("Enter the age of Ram: "))
    shyam_age = int(input("Enter the age of Shyam: "))
    ajay_age = int(input("Enter the age of Ajay respectively: "))

    if ram_age < shyam_age and ram_age < ajay_age:
        print("Ram is youngest")
    elif shyam_age < ram_age and shyam_age < ajay_age:
        print("Shyam is youngest") 
    else:
        print("Ajay is youngest") 

if __name__ == "__main__":
    ages()              