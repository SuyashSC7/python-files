import time
from itertools import product

start=time.perf_counter()
def comb(mylist):
    x = product(mylist, repeat=5)
        
    # Convert the iterator to a list to see all results at once
    all_combinations = list(x)

    print(all_combinations)
    # The iterator is now exhausted and cannot be looped through again

    # To demonstrate, this loop would now do nothing
    for y in x:
        print(y)
ylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
comb(ylist)

stop=time.perf_counter()
print(stop-start)