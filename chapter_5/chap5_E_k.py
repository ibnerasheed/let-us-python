def valid_triangle():
    first_side = int(input("Enter the first side of the triangle: "))
    second_side = int(input("Enter the second side of the triangle: "))
    third_side = int(input("Enter the third side of the triangle: "))
    
    triangle_inequality_valid = (first_side + second_side >= third_side) and \
                                (second_side + third_side >= first_side) and \
                                (first_side + third_side >= second_side)
    
    if triangle_inequality_valid :
        print("valid trinagle")
    else:
        print("Invalid Triangle")    

if __name__ == '__main__':
    valid_triangle()        