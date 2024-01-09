import math

def is_point_inside_or_outside_of_a_circle():
    centre_of_circle_x = float(input("Enter the X cordinate of the circle: "))
    centre_of_circle_y = float(input("Enter the X cordinate of the circle: "))
    radius = float(input("Enter the radius of the circle: "))

    cordinate_x = float(input("Enter the X cordinate of the point to check: "))
    cordinate_y = float(input("Enter the Y cordinate of the point to check: "))
    difference_x = abs(centre_of_circle_x - cordinate_x)
    difference_y = abs(centre_of_circle_y - cordinate_y)
    distance = math.sqrt((difference_x ** 2) + (difference_y ** 2))

    if distance == radius:
        print("The points are on circle")
    elif distance < radius:
        print("The points are inside circle")
    else:
        print("The points are outside circle")    

if __name__ == "__main__":
    is_point_inside_or_outside_of_a_circle()  