str = input("Nhập chuỗi str: ")
hex_chars = "0123456789abcdefABCDEF"
hex_str = ""

for char in str:
    if char in hex_chars:
        hex_str += char

if hex_str == "":
    print("Chuỗi không phải là chuỗi Hex")
else:
    decimal_num = int(hex_str, 16)
    print("Chuỗi Hex:", hex_str)
    print("Số thập phân:", decimal_num)
