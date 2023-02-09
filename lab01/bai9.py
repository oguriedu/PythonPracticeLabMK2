a,b,c=map(float,input("Nhập độ dài 3 cạnh:").split())
cv=a+b+c
p=cv/2; import math
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("chu vi tam giác là:",cv)
print("Diện tích tam giác là:",s)