a = input("Nhập chuỗi ký tự A: ")
b = input("Nhập chuỗi ký tự B: ")

# Chuyển chuỗi sang list để có thể thêm dấu '+'
a_list = list(a)
b_list = list(b)

# Thêm dấu '+' giữa các ký tự của chuỗi
a_list.insert(1, '+')
b_list.insert(1, '+')

# Chuyển list thành chuỗi và tính toán
a = "".join(a_list)
b = "".join(b_list)

try:
    c, d = a.split("+")
    e, f = b.split("+")
    int_c = int(c)
    int_d = int(d)
    int_e = int(e)
    int_f = int(f)
    if int_c + int_d == int_e + int_f:
        print(c + "+" + d + "=" + e + "+" + f)
    else:
        print("Không tồn tại cách đặt!")
except:
    print("Không tồn tại cách đặt!")
