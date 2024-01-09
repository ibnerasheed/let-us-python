def points_in_quadrants():
    X_cordinates = int(input("Enter the X coordinates: "))
    Y_cordinates = int(input("Enter the Y coordinates: "))

    if X_cordinates == 0 and Y_cordinates == 0:
        print("The points are on origin")
    elif X_cordinates == 0 and Y_cordinates != 0:
        print("Points are on Y cordinates")
    elif X_cordinates != 0 and Y_cordinates == 0:
        print("Points are on X cordinates")    
    elif X_cordinates > 0 and Y_cordinates > 0:
        print("Points are in first quadrant")
    elif X_cordinates < 0 and Y_cordinates > 0:
        print("Points are in second quadrant")
    elif X_cordinates < 0 and Y_cordinates < 0:
        print("Points are in third quadrant")   
    else:
        print("Points are in fourth quadrants")     

if __name__ == "__main__":
    points_in_quadrants()  


