from tabulate import tabulate 
hour = int (input('nhập số điện đã dùng: '))
cong_suat_dien = (220*2.7)
dien_nang_tieu_thu = cong_suat_dien*(hour/3600)
tien_dien = dien_nang_tieu_thu*7000
a = [[cong_suat_dien, dien_nang_tieu_thu, tien_dien]]
name = ['công suất điện', 'điện năng tiêu thụ', 'tiền điện']
print (tabulate(a,headers=name, tablefmt='fancy_grid'))

