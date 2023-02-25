#tính tổng 
n=int(input("nhập n = "))
tongS1=0
while n<=0:
    print("hãy nhập lại số cho đúng")
    n=int(input("nhập n = "))
for i in range(1,n+1):
    tongS1=tongS1+i
print("giá trị của tổng S1 = ",tongS1)