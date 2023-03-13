n = input("Nhập chuỗi Str: ")
n = n.upper()

for char in n:
    if not char.isdigit() and char not in ['A', 'B', 'C', 'D', 'E', 'F']:
        n = n.replace(char, '')
print(n)
decimal = int(n, 16)
print("Số thập phân:", decimal)
