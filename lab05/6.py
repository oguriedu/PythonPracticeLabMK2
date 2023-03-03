hex_str = input ("Nhập một chuỗi Str từ bàn phím: ") 
valid_str = "" 
for ch in hex_str: 
    if ch in "0123456789ABCDEF": 
        valid_str += ch 
        decimal_val = int(valid_str, 16) 
    print("Chuỗi số thập phân là:", decimal_val)