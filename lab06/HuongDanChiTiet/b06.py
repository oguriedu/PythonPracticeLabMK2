hoten = input('Nhập họ tên sinh viên: ')
lst = hoten.strip().split(" ")  # hàm split(" ") chuyển chuỗi hoten thành list lst
ten = lst[len(lst)-1]
print("Tên sinh viên là:", ten)
