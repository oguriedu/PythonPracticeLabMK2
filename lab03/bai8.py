n=int(input("nhập n: "))
a=0
b=0
c=0
for i in range(1,n+1):
    a+=i
    c+=2*i
for i in range(n+1):
    b+=2*i+1
print("đáp án câu a",a)
print("đáp án câu b",b)
print("đáp án câu c",c)