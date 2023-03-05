# Nhập chuỗi ký tự Str từ bàn phím
Str = input("Nhập chuỗi ký tự: ")

# Xóa tất cả các ký tự không phải số trong chuỗi
numbers_only = ""
for char in Str:
    if char.isdigit():
        numbers_only += char

# In ra chuỗi số
print("Chuỗi số:", numbers_only)

# Kiểm tra xem chuỗi số có phải là số hoàn hảo hay không
num = int(numbers_only)
divisors = []
for i in range(1, num):
    if num % i == 0:
        divisors.append(i)

if sum(divisors) == num:
    print("Đây là số hoàn hảo.")
else:
    print("Đây không phải là số hoàn hảo.")
