tai_khoan = 0
lst_yeu_cau = []
while True:
    yeu_cau = input("Nhập giao dịch (D hoặc W số_tiền hoặc 0 để kết thúc): ")
    if yeu_cau == "0":
        break
    else:
        lst_yeu_cau.append(yeu_cau)
for yeu_cau in lst_yeu_cau:
    loai_yeu_cau, so_tien = yeu_cau.split()
    so_tien = int(so_tien)
    if loai_yeu_cau == "D":
        tai_khoan = tai_khoan + so_tien
    elif loai_yeu_cau == "W":
        tai_khoan = tai_khoan - so_tien

print("Số tiền thực trong tài khoản là:", tai_khoan)
