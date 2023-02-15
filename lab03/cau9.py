n=int(input("nhập n: "))
a=0
b=0
c=0
while n<0:
    print("n nhỏ hơn 0 mời nhập lại")
    n=int(input("nhập n: "))
for i in range(1,n+1):
    a=a+i*i
    b=(2*i)**4
for i in range(n+1):
    b+=(2*i+1)**3
print("đáp án câu a",a)
print("đáp án câu b",b)
print("đáp án câu c",c)