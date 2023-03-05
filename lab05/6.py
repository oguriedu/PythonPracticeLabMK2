str=input("Nhập chuỗi cần kiểm tra:")
str=str.lower()
hex= set("0123456789abcdef")
if all(c in hex for c in str):
    thap_phan=int(str,16)
    print("Chuỗi",str,"là số hex, tương ứng với số thập phân là",thap_phan)
else:
    loc_hex = [c for c in str if c in hex]
    loc_str= ''.join(loc_hex)
    thap_phan=int(loc_str,16)
    print("Chuỗi",str,"Không phải là số hex , đã loại bỏ kí tự không hợp lệ và chuyển sang thập phân",thap_phan)