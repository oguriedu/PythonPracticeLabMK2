import math
x=float(input("nhập vào x: "))
while x<=0 or x==1:
    print("điều kiện của pt là: x>0 hoặc x khác 1 ") 
    x=float(input("nhập lại x: "))
f=math.log(x,4)+math.log(2,x)
print("kết quả của phương trình là: ",round(f,2))
