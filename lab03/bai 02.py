j = []
def kiem_tra(n):
    tong = 0
    for i in range(1, n // 2 + 1):
        if (n % i == 0):
            tong += i
    if (tong == n):
        return True
    else:
        return False
n = int(input("Nhập vào số N lớn hơn 0: "))
for i in range(1,n+1):
    if kiem_tra(i):
        j.append(i)
print(i,"các số hoàn hảo nhỏ hơn n là: ")
print(j)
