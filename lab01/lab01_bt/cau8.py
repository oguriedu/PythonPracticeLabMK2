A=[]
B=[]
C=[]
O=[]
a1=int(input('Length of A,B,C: '))
for i in range(a1):
    a=int(input("Enter the element of A:"))
    A.append(a)

for y in range(a1):
    b=int(input('Enter the element of B:'))
    B.append(b)
for z in range(a1):
    c=int(input("Enter the element of C:"))
    C.append(c)
for t in range(0,len(A)):
    O.append((A[t]+B[t]+C[t])/3)
print(A)
print(O)
