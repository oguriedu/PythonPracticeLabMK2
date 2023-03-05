a=input("nhập chuỗi ký tự từ bàn phím: ")
b=""
for i in a:
    if i.isnumeric():
        b+=i
print(b)
c=int(b)
d=0
for i in range(1,c):     
    if (c%i==0):
            d=d+i
if d==c:
    print(c,"là số hoàn hảo")
if d!=c:
     print(c,"không phải là số hoàn hảo")