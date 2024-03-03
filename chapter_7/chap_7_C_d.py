def positive_negative_list(list):
    positive_list = []
    negative_list = []
    
    for num in list:
        if num > 0:
            positive_list.append(num)
        else:
            negative_list.append(num)  

    return positive_list, negative_list    

def main():
    list = [6, 9, 11, -2]
    print(positive_negative_list(list))

if __name__ == "__main__":
    main()      
