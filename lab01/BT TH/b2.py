d =float (input("Nhập số ngày: "))
h =float (input("Nhập số giờ: "))
m =float(input("Nhập số phút: "))
s =float(input("Nhập số giây: "))
giay = d * 24 * 60 * 60 + h * 60 * 60 + m * 60 + s
phut = d * 24 * 60 + h * 60 + m + s/60
gio = d * 24 + h + m/60 + (s/60)/60
ngay = d + h/24 + (m/60)/24 + ((s/60)/60)/24

print(f'Đổi ra giây: {giay:.5f} giây')
print(f'Đổi ra phút: {phut:.2f} phút')
print(f'Đổi ra giờ: {gio:.2f} giờ')
print(f'Đổi ra ngày: {ngay:.2f} ngày')
