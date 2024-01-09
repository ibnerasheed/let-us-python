def main():
    strings = 'Light travels faster than sound. This is why some people appear bright until you hear them speak.'
    updated_string = strings.replace('Light','LIGHT').replace('sound','SOUND')
    print(updated_string)

if __name__ == '__main__':
    main()