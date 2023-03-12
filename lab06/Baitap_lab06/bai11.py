import random


n=int(input('Nhập số phần tử list A:'))
a=[]
for i in range(n):
    a.append(int(input('Nhập các phần tử:')))
print(a)
#1
B=[i for i in a if(i%3==0 and i%5!=0)]
print('List B:',B)
#2
C=[i**2 for i in a]
print('List C:',C)
#3
D=random.sample([i for i in a if i%3==0],k=1)
print('List D:',D)