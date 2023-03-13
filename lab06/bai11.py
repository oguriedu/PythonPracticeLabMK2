import random

A = [int(i) for i in input().split()]

B = [int(i) for i in A if i%3==0 and i%5!=0]

print('B:',B)

C=A.copy()

print('C:',C)

C=[]

D=[]

for i in random.choices(A,k=len(A)):

    if i%3==0:

        D.append(i)

print('D:',D)