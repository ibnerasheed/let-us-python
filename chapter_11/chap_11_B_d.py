def compute(dict_1: dict, dict_2: dict) -> int:
    total = 0

    for key in dict_1:
        sum = dict_1[key] * dict_2[key]
        total += sum
    return total


def main():
    dict1 = {
        'aalo': 40,
        'pyaaz': 100,
        'mutton':  800
    }
    dict2 = {
        'aalo': 10,
        'pyaaz': 10,
        'mutton':  3
    }

    print(f'Total cost is : Rs.{compute(dict1, dict2)}')


if __name__ == '__main__':
    main()
