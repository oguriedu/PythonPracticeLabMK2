import random

n = int(input("Nhap n: "))
A = []
for i in range(n):
    num = int(input(f"Nhap so thu {i+1}: "))
    A.append(num)

B = [num for num in A if num % 3 == 0 and num % 5 != 0]
print("Danh sach cac so chia het cho 3 nhung khong chia het cho 5 la: ", B)

C = [num**2 for num in A]
print("Danh sach sau khi binh phuong la: ", C)

D = random.sample([num for num in A if num % 3 == 0], k=3)
print("3 phan tu ngau nhien chia het cho 3: ", D)
