bđ=int(input("Nhập giờ bắt đầu: "))
kt=int(input('Nhập giờ kêt thúc: '))
while (bđ<5)or(bđ>22)or(kt>22):
    print("Thời gian cho thuê phải sau 5h trước 22h. Mời nhập lại!")
    bđ=int(input("Nhập giờ bắt đầu: "))
    kt=int(input('Nhập giờ kêt thúc: '))
tgianthue=kt-bđ
if tgianthue <=3:
    tiensan=tgianthue*100000
else:
    tiensan=300000+(tgianthue-3)*75000
if (bđ>=11)and(kt<=15):
    print('Tiền sân phải trả: ',tiensan-(tiensan*0.1),'đồng')
else:
    print('Tiền sân phải trả: ',tiensan,'đồng')