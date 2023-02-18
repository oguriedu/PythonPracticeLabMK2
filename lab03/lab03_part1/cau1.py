
tong=int(0)
n=int(input("Nhập n: "))
for i in range(0,n):
    tong+=(2*(i+1))/(2*i+3)
    i+=1
print("tong = %0.3f"%(tong+1))