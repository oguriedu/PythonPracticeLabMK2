n = int(input("Nhập giá trị của n: "))

for num in range(1, n):
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    if sum_divisors == num:
        print(num)
