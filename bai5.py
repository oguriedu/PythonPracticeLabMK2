Str = input("Nhập chuỗi ký tự: ")

# Xóa tất cả các ký tự không phải số
so = ''
for i in range(len(Str)):
    if Str[i].isnumeric():
        so += Str[i]

print("Chuỗi số sau khi xóa các ký tự không phải số:", so)

# Kiểm tra xem số đó có phải số hoàn hảo hay không
tong_uoc = 0
so = int(so)
for i in range(1, so):
    if so % i == 0:
        tong_uoc += i

if tong_uoc == so:
    print("Đây là số hoàn hảo.")
else:
    print("Đây không phải là số hoàn hảo.")
