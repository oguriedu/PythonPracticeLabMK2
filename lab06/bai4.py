mylist = []
print('Nhập "0" khi muốn dừng')
while True:
    val = input('Nhập dữ liệu: ')
    if val == '0':
        print('Kết thúc')
        break
    mylist.append(val)
print(mylist)
list=[1,2,3]
# Chèn số vào đầu danh sách
mylist.insert(0, list)
print("Danh sách sau khi chèn", list, "vào đầu danh sách là:")
print(mylist)
# Chèn số vào cuối danh sách
mylist.append(list)
print("Danh sách sau khi chèn", list, "vào cuối danh sách là:")
print(mylist)
# Chèn số vào vị trí thứ 5 của danh sách
if len(mylist) >= 5:
    mylist.insert(4, list)
    print("Danh sách sau khi chèn", list, "vào vị trí thứ 5 là:")
    print(mylist)
else:
    print("Danh sách không đủ dài để chèn vào vị trí thứ 5.")
###Xóa phần tử thứ k
k = int(input("Nhập chỉ số phần tử cần xóa : "))
if k >= 0 and k < len(mylist):
    # Xóa phần tử tại chỉ số k
    del mylist[k]
    print("Danh sách sau khi xóa phần tử thứ", k, "là:")
    print(mylist)
else:
    print("Chỉ số phần tử cần xóa không hợp lệ.")
mylist.sort()
mylist.sort(reverse=True)