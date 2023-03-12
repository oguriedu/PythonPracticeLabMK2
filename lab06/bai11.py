import random
n = int(input("Nhập số phần tử của danh sách: "))
A = []
for i in range(n):
    A.append(int(input(f"Nhập phần tử thứ {i+1}: ")))
B = [num for num in A if num % 3 == 0 and num % 5 != 0]
print("Danh sách A là:", A)
print("Danh sách B là:", B)
C = [num**2 for num in A]
print("Danh sách C là:",C)
D = [num for num in A if num % 3 == 0 and random.choice([True, False])]
print("Danh sách D là:",D)