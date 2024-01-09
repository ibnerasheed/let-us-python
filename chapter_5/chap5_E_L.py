def triangle_type():
    first_side = int(input("Enter the first side of the triangle: "))
    second_side = int(input("Enter the second side of the triangle: "))
    third_side = int(input("Enter the third side of the triangle: "))

    if (first_side + second_side <= third_side) and (second_side + third_side <= first_side) and (first_side + third_side <= second_side):
        print("Invalid trinagle")
    else:
        if first_side == second_side == third_side:
            print("Equilateral Triangle")

        if (first_side == second_side and       