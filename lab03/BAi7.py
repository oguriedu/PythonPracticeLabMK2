def tong_nghich_dao(n):
    tong = 0
    for i in range(1, n+1):
        tong += 1/i
    return tong

n = int(input("Nhập số nguyên dương n: "))
tong = tong_nghich_dao(n)
print("Tổng nghịch đảo của", n, "số nguyên đầu tiên là:", tong)
