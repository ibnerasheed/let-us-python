import operator

def sorting(tuple, index):
    return sorted(tuple, reverse = True, key = operator.itemgetter(index))


def main():
    lst = [('Key', 101.25), ('Lock', 320.85), ('Hammer', 100.55), ('Spanner', 67.77), ('Tong', 93.03)]
    sorted_list = sorting(lst, index = 1)
    print(sorted_list)

if __name__ == "__main__":
    main()      