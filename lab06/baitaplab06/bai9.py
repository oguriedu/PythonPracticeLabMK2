nums = []
while True:
    try:
        x=int(input("nhập số từ bàn phím"))
        nums.append(x)
    except ValueError:
        break
assert all(num % 2 == 0 for num in nums), "List contains odd numbers"
print("tất cả đều là số chẵn")