binary_str = input("Nhập chuỗi nhị phân: ")
decimal = 0
for i in range(len(binary_str)):
    if binary_str[i] == '1':
        decimal += 2 ** (len(binary_str) - i - 1)
print("Số thập phân tương ứng là:", decimal)
