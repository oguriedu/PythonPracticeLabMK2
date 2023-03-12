import random
A = []
for i in range(1000):
    i = random.randint(1,99999)
    A.append(i)
print(A)
A1 = sorted(A)
print('Sắp xếp theo thứ tự tăng dần (dùng hàm sorted):\n',A1)
for i in range(len(A)):
    for j in range(i+1,len(A)):
        if A[j]<A[i]:
            A[j],A[i]=A[i],A[j]
                        
print('Sắp xếp theo thứ tự tăng dần (không dùng hàm sorted):',A)
