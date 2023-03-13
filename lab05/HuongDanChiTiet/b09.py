# Khai báo chuỗi s_in để lưu trữ chuỗi đầu vào
s_in = input("Nhập vào chuỗi cần mã hóa: ")

# Khai báo chuỗi s_out để lưu trữ chuỗi sau khi mã hóa
s_out = ""

# Duyệt từng ký tự trong chuỗi s_in
for char in s_in:
    # Lấy ra mã Unicode của ký tự
    char_code = ord(char)
    # Mã hóa ký tự
    char_code = char_code + 2
    # Chuyển mã Unicode về ký tự
    char = chr(char_code)
    # Thêm ký tự vào chuỗi s_out
    s_out += char
