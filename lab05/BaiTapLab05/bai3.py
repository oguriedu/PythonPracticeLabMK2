x=int(input("Nhập số tự nhiên:"))
print("Số",x,"chuyển từ hệ cơ số 10 sang nhị phân =",end=" ")
k = []
while (x>0):
        a = int((x%2)) 
        k.append(a) 
        x = (x-a)/2 
kq = ""
k.reverse() 
for i in k:
        kq += str(i)
print(kq)