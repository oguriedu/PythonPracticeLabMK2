import math

print("Liệt kê tất cả số nguyên tố có 2 chữ số:")
dem = 0
sum_nguyen_to = 0
for i in range(10, 100):
    ktNT = True
    squareRoot = int(math.sqrt(i))
    for j in range(2, squareRoot + 1):
        if (i % j == 0):
            ktNT = False  # ktNt là biến kiểm tra số nguyên tố
    if ktNT:
        print(i, end=' ')
        dem = dem + 1
        sum_nguyen_to += i
print()
print("Tổng các số nguyên tố có 2 chữ số là:", sum_nguyen_to, end=' ')
print()
print("Số các số nguyên tố có hai chữ số là : ", dem)
