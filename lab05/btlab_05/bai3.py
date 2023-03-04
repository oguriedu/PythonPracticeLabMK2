
n = int(input("Nhap vao so thap phan: "))
k = []
while (n>0):
    a = int(float(n%2)) 
    k.append(a)
    n = (n-a)/2 
kq = ""

k.reverse() 
for i in k:
    kq += str(i)

print("So", n," co dang nhi phan la:", kq)