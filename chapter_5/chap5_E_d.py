def traingle_validity(angle_a, angle_b, angle_c):
    sum_of_angles = (angle_a + angle_b + angle_c)
    
    if sum_of_angles ==  180:
        return True
    else:
        return False


def main():
    angle_a = int(input("Enter the angle A: "))
    angle_b = int(input("Enter the angle B: "))
    angle_c = int(input("Enter the angle C: "))

    sum_of_angles = (angle_a + angle_b + angle_c)

    if traingle_validity(angle_a, angle_b, angle_c):
        print("Valid triangle")
    else:
        print("Invalid triangle")   

if __name__ == "__main__":
    main()  