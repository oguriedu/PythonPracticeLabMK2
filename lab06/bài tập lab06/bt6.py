import random
A=[]
for i in range(1000):
    i=random.randint(1,99999)
    A.append(i)
print("1000 số tự nhiên ngẫu nhiên:\n",A)
#Sắp xếp theo hàm sort
A.sort()
print(A)
#Sắp xếp ko theo hàm sort
for i in range(len(A)):
    for j in range(i+1,len(A)):
        if A[j]<A[i]:
            A[j],A[i]=A[i],A[j]
                        
print("Sắp xếp thứ tự tăng dần:",A)