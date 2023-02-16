#bai1
n = int(input("nhập n:"))
sum=0
def tính(n):
    s=1
    for i in range(n):
        s=s*(2*(i+1))/(2*i+3)
    return s
for i in range(n+1):
    s=tính(i)
    sum +=s
print("tổng dãy số =%0.3f"%(sum))