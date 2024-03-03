def first_character(list):
    char_list = []
    for word in list:
        char_list.append(word[0])
    return char_list    


def main():
    msg = ['Dialogue', 'is', 'dead', 'Chatalogue', 'is', 'in']
    print(first_character(msg))


if __name__ == "__main__":
    main()