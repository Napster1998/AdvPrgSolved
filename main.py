import math

import random
mylist = []
for i in range(0,10):
    x = random.randint(0,100)
    mylist.append(x)
print(mylist)
prime_numbers = []
for i in mylist:
    c = 0
    for j in range(1,i):
        if i%j==0:
            c+=1
    if c == 1:
        prime_numbers.append(i)
print(prime_numbers)
