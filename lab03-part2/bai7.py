#chương trình tính tổng  nghịch đảo của n số nguyên đầu 
tong=0
n=int(input("nhập số n = "))
while n<=0:
    print("hãy nhập lại số n cho chính xác")
    n=int(input("nhập số n = "))
for i in range(1,n+1):
    tong=tong+1/i
print("giá trị của biểu thức S = ",tong)