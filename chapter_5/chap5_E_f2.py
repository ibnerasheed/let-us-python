def rect_area(length, breadth):
    area = length * breadth
    return area

def rect_perimeter(length, breadth):
    return 2*(length + breadth)   


def main():
    length = int(input("Enter the length: "))
    breadth = int(input("Enter the breadth: "))  

    area = rect_area(length, breadth)
    perimeter = rect_perimeter(length, breadth)

    if area > perimeter :
        print("Area is greater than perimeter")
    else:
        print("Area is smaller than perimeter")    
          

if __name__ == "__main__":
    main()     
        


             