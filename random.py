import numpy as np

list3 = []
for i in range(-100,100):
  list3.append(np.random.randint(-100,100))
print("Random numbers list: ",list3)
index_list = []
for j in list3:
  if j >= 0:
    index_list.append(list3.index(j))
print("Index of positive numbers list: ",index_list)
