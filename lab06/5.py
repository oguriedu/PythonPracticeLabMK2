# Viết chương trình sinh một dãy list A gồm 1000 số tự nhiên, nằm ngẫu nhiên trong 
# khoảng [1,99999]
import random
A=[]
for i in range(1000):
    i=random.randint(1,99999)
    A.append(i)
print("1000 số tự nhiên ngẫu nhiên:\n",A)
