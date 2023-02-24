n = int(input("Nhập n: "))
sum = 0

for i in range(1, n+1):
    sum += 1/i

print("Tổng nghịch đảo của", n, "số nguyên đầu tiên là:", sum)