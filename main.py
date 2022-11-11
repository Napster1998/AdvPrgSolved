import math

import random
myList = []
for i in range(1,10):
    x = random.randint(1,100)
    myList.append(x)
print(myList)
prime_numbers = []
indexes = []
for index, i in enumerate(myList):
    a = 0
    for j in range(2,i):
        if i%j==0:
            a+=1
    if a == 0:
        prime_numbers.append(i)
        indexes.append(index)
    a = 0
print(prime_numbers)
print(indexes)




