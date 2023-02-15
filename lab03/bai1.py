#tính giá trị biểu thức
n=int(input("nhập giá trị của n = "))
tong=0
a=1
for i in range(n):
    thua_so=(2*(i+1))/(2*i+3)
    print("thừa số bằng = ",thua_so)
    a=a*thua_so
    print(a)
    tong=tong+a
print("tổng giá trị = ",tong+1)
