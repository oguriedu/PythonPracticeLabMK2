n = int(input("Nhap n: "))
print("Danh sach cac so hoan hao nho hon n: ")
for num in range(1, n):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if num == sum:
        print(num)