def word_frequency(string: str) -> dict:
    frequency = {}

    for word in string:
        if word in frequency:
            frequency[word] += 1

        else:
            frequency[word] = 1
    return frequency


print(word_frequency("adil rasheed"))
