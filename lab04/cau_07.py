n = int(input("Hay nhap so n:"))
m = int(input("Hay nhap so m:"))
i = 0
j = 0
while True:
    i += 1
    j += 1
    if i > n and i % n == 0 and j > m and j % m == 0 and i == j:
        print(i)
        break

