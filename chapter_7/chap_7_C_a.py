list_odd = [1, 3, 5, 7, 9]
list_even = [2, 4, 6, 8]

list_odd[3] = list_even
print(f"the new list is: {list_odd}")

flatten_list = []

#use extend than append as its more computationaly viable. append add each element in in iterations unlike extend
for i in list_odd:
    if isinstance(i, list):
        flatten_list.extend(i)
    else:
        flatten_list.append(i)   

print(flatten_list)  
flatten_list.sort()
print(flatten_list)
