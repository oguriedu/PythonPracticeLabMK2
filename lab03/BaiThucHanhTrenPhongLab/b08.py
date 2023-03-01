n = int(input("Nhap n: "))
sum_a = 0
sum_b = 0
sum_c = 0
for i in range(1, n+1):
    sum_a = sum_a + i
    sum_b = sum_b + (2*i + 1)
    sum_c = sum_c + 2*i
print(f"S1 = 1 + 2 + 3 + … + n = {sum_a}")
print(f"S2 = 1 + 3 + 5 + … + (2n+1) = {sum_b}")
print(f"S3 = 2 + 4 + 6 + … + 2n = {sum_c}")
