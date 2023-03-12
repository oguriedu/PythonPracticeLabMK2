import random

# Tạo dãy list A gồm 1000 số tự nhiên trong khoảng [1,99999]
A = [random.randint(1,99999) for i in range(1000)]

# Sắp xếp lại theo thứ tự tăng dần bằng hàm sorted()
A_sorted = sorted(A)

# In ra 10 phần tử đầu tiên của dãy A_sorted
print(A_sorted[:10])