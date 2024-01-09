"""random()uses 0 < x < 1"""
import random 
import datetime
def main():
    seed_value = datetime.time()
    random.seed(seed_value)
    print(random.randint(10,50))
    print(random.randint(10,50))
    print(random.randint(10,50))
    print(random.randint(10,50))
    print(random.randint(10,50))



    
    
    
    

if __name__ == "__main__":
    main()    