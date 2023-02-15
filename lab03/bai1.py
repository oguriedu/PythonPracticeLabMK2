#1
n=int(input('Nhap n: '))
sum,j = 1, 1
for i in range(0,n+1):
    j*=((2*i+2)/(2*i+3))
    sum+=j
print(round(sum,3))

#2
n=int(input('Nhập n: '))
print('Số hoàn hảo nhỏ hơn n là: ',end="")
for i in range(1,n):
    tong = 0
    for j in range(1, i):
        if (i % j) == 0:
            tong += j
    if tong == i:
        print(i,end=' ')

#3
import math
n=int(input("nhập giá trị n: "))
if n<0:
    print("nhập số tự nhiên: ")
elif n<2:
    print("{} không là số nguyên tố ",format(n))
else:
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i ==0:
            print("{} không là số nguyên tố".format(n))
            break
    else:
        print("{} là số nguyên tố".format(n))

#4
n=int(input('Nhập n: '))
print('Số nguyên tố nhỏ hơn hoặc bằng n là: ',end='')
for i in range(1,n+1):
    check=True
    if (i<2):
        continue
    for j in range(2,i):
        if (i % j == 0):
           check = False
    if check == False:
        continue
    print(i,end=' ')

#5
a=int(input("Nhập chiều rộng hcn: "))
b=int(input("Nhập chiều dài hcn: "))
print("Mô hình ngôi sao hcn")
for i in range(a):
    for j in range(b):
        print('*',end ='')
    print()
#6
n=int(input('Nhập n:'))
sum=0
for i in range(1,n+1):
    sum+=(i**3)
print('Tổng bậc 3 của n số nguyên đầu tiên là:',sum)