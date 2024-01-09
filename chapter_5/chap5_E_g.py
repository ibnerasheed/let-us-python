def collinear():
    x1 = int(input("Enter the first cordinates of x: "))
    y1 = int(input("Enter the first cordinates of y: "))
    x2 = int(input("Enter the second cordinates of x: "))
    y2 = int(input("Enter the second cordinates of y: "))
    x3 = int(input("Enter the third cordinates of x: "))
    y3 = int(input("Enter the third cordinates of y: "))

    slope_first = (float(abs(y2 - y1) / abs(x2 - x1)))
    slope_second = (float(abs(y2 - y3) / abs(x2 - x3)))
    slope_third = (float(abs(y3 - y1) / abs(x3 - x1)))

    if slope_first == slope_second == slope_third:
        print("The points are collinear")
    else:
        print("The are not collinear")    

if __name__ == "__main__":
    collinear()          