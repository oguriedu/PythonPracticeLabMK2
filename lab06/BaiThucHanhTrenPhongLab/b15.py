# Nhập vào danh sách các tuple
lst = [("A", 77, 20), ("K", 30, 53), ("C", 64, 1), ("M", 23, 44)]

new_lst = sorted(lst, key=lambda item: (item[0], item[1], item[2]))

for item in new_lst:
    print(item)
