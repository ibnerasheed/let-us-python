def upper_case(list):
    new_list = []
    for i in list:
        if i.islower():
            upper = i.upper()
            new_list.append(upper)
        else:
            new_list.append(i)    
    return new_list

lst = ['abc', 'def', 'ghi', 'jkl', 'lmn', 'ASD']
print(upper_case(lst))