n=int(input('Nhập n:'))
tong=0
if n<=0:
    print("Nhập lại:")
for i in range(0,n+1):
    tong+=(2*i)**4
print(tong)
