import math
x=float(input("nhập vào x: "))
while x<=0 or x==1:
    print("điều kiện của pt là: x>0 hoặc x khác 1 ") 
    x=float(input("nhập lại x: "))
f=math.log(4,x)+math.log(x,2)
print("kết quả của phương trình là: ",round(f,2))