bd = float(input('Nhập giờ bắt đầu (>5):'))
kt = float(input('Nhập giờ kết thúc (<22):'))
tg = kt-bd
tien = tg*100

def tien_km():
    km = 0
    if tg > 3:
        km += 25*(tg-3)
    if bd>=11 and kt<=15:
        km += tien*0.1
    return km
km = tien_km()
print('số tiền phải trả=%f'%(tien-km))