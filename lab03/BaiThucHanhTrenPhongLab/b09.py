n = int(input("Nhap n: "))
if (n <= 0):
    print("Yeu cau nhap n lon hon 0")
else:
    sum_a = 0
    sum_b = 0
    sum_c = 0
    for i in range(1, n+1):
        sum_a = sum_a + i**2
        sum_b = sum_b + (2*i + 1)**3
        sum_c = sum_c + (2*i)**4
    print(f"S4 = 1^2 + 2^2 + 3^2 + … + n^2 = {sum_a}")
    print(f"S5 = 1^3 + 3^3 + 5^3 + … + (2n+1)^3 = {sum_b}")
    print(f"S6 = 2^4 + 4^4 + 6^4 + … + (2n)^4 = {sum_c}")
