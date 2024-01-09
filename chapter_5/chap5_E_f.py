def area_is_greater_than_perimeter():
    length = int(input("Enter the length: "))
    breadth = int(input("Enter the breadth: "))
    area = length * breadth
    perimeter = 2 * (length + breadth)

    if area > perimeter:
        print("The area is greater than it's perimeter")
    else:
        print("The area is less than it's perimeter")

if __name__ == "__main__":
    area_is_greater_than_perimeter()          