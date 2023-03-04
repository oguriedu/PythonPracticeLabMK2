a=input("nhập chuỗi ký tự từ bàn phím: ")
t=""
for i in a:
    if i.isnumeric():
        t+=i
print(t)
l=int(t)
h=0
for i in range(1,l):     
    if (l%i==0):
            h=h+i
if h==l:
    print(l,"là số hoàn hảo")
if h!=l:
     print(l,"không phải là số hoàn hảo")