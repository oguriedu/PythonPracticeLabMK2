# a=int(input('Nhập vào số nguyên có 3 chữ số :'))
# # if a in[100,200,300,400,500,600,700,800,900]:
#     #  print
# if a>100 and a<=999:
#     print('Cách đọc số',a,'là %d trăm %d mươi %d'%((a/100%10),(a%100/10),(a%100%10)))
# else:
#     print('b nhập không hợp lệ')
day=['','Một','Hai','Ba','Bốn','Năm','Sáu','Bảy','Tám','Chín']
day1=['','Mười','Hai','Ba','Bốn','Năm','Sáu','Bảy','Tám','Chín']
day2=['','Một','Hai','Ba','Tư','Năm','Sáu','Bảy','Tám','Chín']
a=int(input('Nhập số nguyên có 3 chữ số: '))
hang_tram=a//100
hang_chuc=(a-hang_tram*100)//10
don_vi=a-hang_tram*100-hang_chuc*10
if hang_tram==0:
    print(f"{day1[hang_chuc]} {day[don_vi]}")
else:
    if hang_chuc==0 and don_vi!=0:
        print(f"{day[hang_tram]} Trăm lẻ {day2[don_vi]}")
    else:
        print(f"{day[hang_tram]} Trăm {day1[hang_chuc]} {day2[don_vi]}")