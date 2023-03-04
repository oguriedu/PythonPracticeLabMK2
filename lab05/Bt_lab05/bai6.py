def is_hex_string(Str):
    Str = Str.upper()
    hex_chars = "0123456789ABCDEF"
    for char in Str:
        if char not in hex_chars:
            Str = Str.replace(char, "")
    return int(Str, 16)

Str = input("Nhập một chuỗi Str từ bàn phím: ")
decimal_num = is_hex_string(Str)
print("Số thập phân của chuỗi là:", decimal_num)
