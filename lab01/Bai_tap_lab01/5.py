a = [int(x) for x in input('Nhập vector a: ').split()]
b = [int(x) for x in input('Nhập vector b: ').split()]
result = sum(x * y for x, y in zip(a, b))
print("Tích vô hướng của 2 vector là:", result)