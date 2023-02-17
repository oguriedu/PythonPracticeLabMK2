s= 0
n = int(input("Nhập vào số n: "))
while n<0:
    n = int(input("Nhập vào số n: "))

for i in range(1, n + 1) :
    s+= (2*i+1)**3
 
print("Tổng số là: ",s)