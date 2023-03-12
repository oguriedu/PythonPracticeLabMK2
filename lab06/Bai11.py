import random
A=[]
while True:
    n=int(input('Nhập phần tử của list( Nhập 0 để dừng): '))
    if n==0:
        break
    A.append(n)
print(f'List A: {A}')
B=[i for i in A if (i%3==0) and (i%5!=0)]
print(f'List B: {B}')
C=[i**2 for i in A]
print(f'List C: {C}')
D=[]
x=[i for i in A if i%3==0]
D.append(random.choice(x))
print(f'List D: {D}')
