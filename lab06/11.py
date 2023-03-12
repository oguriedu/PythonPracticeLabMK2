import random

n = int(input("Nhập số phần tử của list A: "))
a = [int(input()) for i in range(n)]

# a. Tạo listB chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5 từ list ban đầu
b = [x for x in a if x % 3 == 0 and x % 5 != 0]
print("List B: ", b)

# b. Tạo listC với các phần tử là bình phương của ListA
c = [x**2 for x in a]
print("List C: ", c)

# c. Tạo listD gồm các phần tử lấy ngẫu nhiên từ ListA mà chia hết cho 3
d = [x for x in a if x % 3 == 0]
random.shuffle(d)
print("List D: ", d)
