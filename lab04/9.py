def bac(n):
    tong = 0
    while (n > 0):
        tong = tong + n % 10
        n = int(n / 10)
    return tong

n = int(input("Nhập số nguyên dương n = "))
print("Tổng các chữ số của", n , "là", bac(n))