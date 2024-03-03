def fer_cel(fer):
    return int(5 / 9 * (fer - 32))

def main():
    temp_fer = [212, 120, 100, 93, 37]
    temp_celc = []
    for temp in temp_fer:
        temp_celc.append(fer_cel(temp))

    print(temp_celc)    

if __name__ == "__main__":
    main() 