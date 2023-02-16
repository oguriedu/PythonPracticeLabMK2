# In ra số nguyên tố gần nhất với n
n=int(input("Nhập n:"))
flag=True
for i in range(2,n):
    if(n%i==0):
        flag=False
if flag==False:
    print(n,"không phải là số nguyên tố")

    for i in range(2,n):
        flag1=True
        t=n-i
        for j in range(2,t):
            if t%j==0:
                flag1=False
        if flag1==True:
            print(t,"là số nguyên tố gần nhất bên trái",n)
            break
    for i in range(2,n):
        flag1=True
        t=n+i
        for j in range(2,t):
            if t%j==0:
                flag1=False
        if flag1==True:
            print(t,"là số nguyên tố gần nhất bên phải",n)
            break
else:
    if flag==True:
        print(n,"là số nguyên tố ")

            
        
    