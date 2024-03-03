import random

def occurance(list, number):
    count = 0
    for i in range(len(list)):
        if number == list[i]:
            count+=1
            return i
        else:
            return -1
    return count    
        
        
            


list_random = random.sample(range(0,100), 10)
print(occurance(list_random, 4))

# print(list_random)

