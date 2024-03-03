def remove_duplicates(list):
    list_without_duplicates = []
    for num in list:
        if num not in list_without_duplicates:
            list_without_duplicates.append(num)
    return list_without_duplicates    

def main():
    list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 10, 20, 68, 8, 40, 45, 1, 5, 53, 45, 17]
    print(remove_duplicates(list))

if __name__ == "__main__":
    main()



