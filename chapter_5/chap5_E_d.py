def valid_triangle():
    angle_a = int(input("Enter the angle A: "))
    angle_b = int(input("Enter the angle B: "))
    angle_c = int(input("Enter the angle C: "))

    sum_of_angles = (angle_a + angle_b + angle_c)

    if sum_of_angles ==  180:
        print("Valid triangle")
    else:
        print("Invalid triangle")   

if __name__ == "__main__":
    valid_triangle()   