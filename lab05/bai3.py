n = int(input("Nhập số tự nhiên n: "))

binary_list = []
while n > 0:
    binary_list.append(n % 2)
    n //= 2

binary_str = ''.join(str(bit) for bit in reversed(binary_list))

print("Số nhị phân tương ứng là:", binary_str)
