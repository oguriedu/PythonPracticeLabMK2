# Khai báo chuỗi s_in để lưu trữ chuỗi cần giải mã
s_in = input("Nhập vào chuỗi cần giải mã: ")

# Khai báo chuỗi s_out để lưu trữ chuỗi sau khi giải mã
s_out = ""

for char in s_in:
    char_code = ord(char)  # Chuyển ký tự sang mã Unicode
    char_code -= 2  # Trừ 2 từ mã Unicode
    s_out += chr(char_code)  # Chuyển mã Unicode sang ký tự và thêm vào s_in
print('Chuỗi sau khi giải mã:', s_out)
