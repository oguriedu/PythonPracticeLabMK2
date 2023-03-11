mylist = []
print('Nhập "0" khi muốn dừng')
while True:
    val = input('Nhập dữ liệu: ')
    if val == '0':
        print('Kết thúc')
        break
    mylist.append(val)
print(mylist)
m = input("Nhập số cần chèn: ")
# Chèn số vào đầu danh sách
mylist.insert(0, m)
print("Danh sách sau khi chèn", m, "vào đầu danh sách là:")
print(mylist)
# Chèn số vào cuối danh sách
mylist.append(m)
print("Danh sách sau khi chèn", m, "vào cuối danh sách là:")
print(mylist)
# Chèn số vào vị trí thứ 5 của danh sách
if len(mylist) >= 5:
    mylist.insert(4, m)
    print("Danh sách sau khi chèn", m, "vào vị trí thứ 5 là:")
    print(mylist)
else:
    print("Danh sách không đủ dài để chèn vào vị trí thứ 5.")
