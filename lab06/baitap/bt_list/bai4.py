mylst = []
print('Nhập "0" khi muốn dừng')
while True:
    val = input('Nhập dữ liệu: ')
    if val == '0':
        print('Kết thúc')
        break
    mylst.append(val)
print(mylst)
list=[1,2,3]
# Chèn số vào đầu danh sách
mylst.insert(0, list)
print("Danh sách sau khi chèn", list, "vào đầu danh sách là:")
print(mylst)
# Chèn số vào cuối danh sách
mylst.append(list)
print("Danh sách sau khi chèn", list, "vào cuối danh sách là:")
print(mylst)
# Chèn số vào vị trí thứ 5 của danh sách
if len(mylst) >= 5:
    mylst.insert(4, list)
    print("Danh sách sau khi chèn", list, "vào vị trí thứ 5 là:")
    print(mylst)
else:
    print("Danh sách không đủ dài để chèn vào vị trí thứ 5.")
###Xóa phần tử thứ k
k = int(input("Nhập chỉ số phần tử cần xóa : "))
if k >= 0 and k < len(mylst):
    # Xóa phần tử tại chỉ số k
    del mylst[k]
    print("Danh sách sau khi xóa phần tử thứ", k, "là:")
    print(mylst)
else:
    print("Chỉ số phần tử cần xóa không hợp lệ.")
mylst.sort()
mylst.sort(reverse=True)