n = input("Nhap chuoi ky tu: ")
t = ""
for i in n:
    if i.isnumeric():
        t += i
print(t)
l = int(t)
h = 0
for i in range(1,l):     
    if (l % i == 0):
            h = h + i 
if h == l:
    print(l,"La so hoan hao")
if h != l:
     print(l,"Khong phai so hoan hao")