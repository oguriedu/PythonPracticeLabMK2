import numpy as t
import math
A1=[]
B1=[]
while True:
    a=input("Enter the element of vector A:")
    if a=='e':
        break
    A1.append(a)
    A=t.array(A1)
while True:
    b=input("Enter the element of vector B: ")
    if b=='e':
        break
    B1.append(b)
    B=t.array([B1])
c=eval(input('Enter angle: '))
lAl=t.linalg.norm(A)
lBl=t.linalg.norm(B)
print('Scalar of vector A and B :',round(lAl*lBl*math.cos(c),2))