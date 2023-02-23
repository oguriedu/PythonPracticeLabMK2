import math
n=int(input("nhập số nguyên dương n: "))
while n<0:
    print("mời nhập lại")
    n=int(input("nhập số nguyên dương n: "))
a=0
b=0
c=0
i=0
while i<=n:
    print(i)
    if i>0: 
        a=a+i*i
        b+=math.pow(2*i +1,3)
    c+=math.pow(2*i,3)
    i+=1
print("kết quả của câu a là",a)
print("kết quả của câu b là",b)
print("kết quả của câu c là",c)


