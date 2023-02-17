s=0
n=int(input("Nhập số nguyên dương : "))
while  n<0:
    n=int(input("Nhập số nguyên dương : "))
for i in range(1,n+1):
    s+=i/1
print("Tổng nghịch đảo của ",n,"số nguyên đầu tiên là: ",s)