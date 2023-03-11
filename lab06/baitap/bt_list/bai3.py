lst = []
print('Nhập "0" khi muốn dừng')
while True:
    val = input('Nhập dữ liệu: ')
    if val == '0':
        print('Kết thúc')
        break
    lst.append(val)
print(lst)
m = input("Nhập số cần chèn: ")
# Chèn số vào đầu danh sách
lst.insert(0, m)
print("Danh sách sau khi chèn", m, "vào đầu danh sách là:")
print(lst)
# Chèn số vào cuối danh sách
lst.append(m)
print("Danh sách sau khi chèn", m, "vào cuối danh sách là:")
print(lst)
# Chèn số vào vị trí thứ 5 của danh sách
if len(lst) >= 5:
    lst.insert(4, m)
    print("Danh sách sau khi chèn", m, "vào vị trí thứ 5 là:")
    print(lst)
else:
    print("Danh sách không đủ dài để chèn vào vị trí thứ 5.")