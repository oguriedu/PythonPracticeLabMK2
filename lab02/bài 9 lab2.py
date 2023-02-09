so_dien = int(input("nhập số điện đã tiêu thụ hộ tui: "))
tien_dien = 0

if so_dien > 300:
    so_dien_tinh_toan = so_dien - 300
    tien_dien += 5000 * so_dien_tinh_toan
    so_dien -= so_dien_tinh_toan

if so_dien > 200:
    so_dien_tinh_toan = so_dien - 200
    tien_dien += 3000 * so_dien_tinh_toan
    so_dien -= so_dien_tinh_toan

if so_dien > 100:
    so_dien_tinh_toan = so_dien - 100
    tien_dien += 2500 * so_dien_tinh_toan
    so_dien -= so_dien_tinh_toan

tien_dien += 2000 * so_dien

print("số tiền điện mà bạn phải trả cho tui là:", tien_dien)