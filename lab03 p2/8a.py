n=int(input("Nhập n:"))
tong=0
if n<=0:
    print("Nhập lại:")
else:
    for i in range(0,n):
        i+=1
        tong+=i
print(tong)
