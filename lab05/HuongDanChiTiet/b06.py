# c1
str = input('Nhập họ tên sinh viên: ')
ten = ''
pos = len(str)
while str[pos-1] != " ":
    pos -= 1
for i in range(pos, len(str)):
    ten += str[i]
print("Tên sinh viên là:", ten)

# c2
str = input('Nhập họ tên sinh viên: ')
pos = str.rfind(" ")
print("Tên sinh viên là:", str[pos+1:])

# c3
hoten = input('Nhập họ tên sinh viên: ')
lst = hoten.strip().split(" ")  # hàm split(" ") chuyển chuỗi hoten thành list lst
ten = lst[len(lst)-1]
print("Tên sinh viên là:", ten)
