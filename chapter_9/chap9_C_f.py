def remove_empty_tuples(list_tuples):
    new_list = []
    for tuple in list_tuples:
        if len(tuple) != 0:
            new_list.append(tuple)
    return new_list


def main():
    lst1= [( ), ('Paras', 5), ('Ankit', 11), ( ), ('Harsha', 115), ('Aditya', 115), ( ), ('Aditi', 3), ( )]
    print(remove_empty_tuples(lst1))


if __name__ == "__main__":
    main()    