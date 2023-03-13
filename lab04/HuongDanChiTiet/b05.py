print('Nhập số ban đầu :',end=' ')
soBanDau = int(input())    
temp=soBanDau
#Sử dụng cấu trúc rẽ nhánh xử lý trường hop n < 0
if soBanDau < 0:
    print("Xin mời nhập số tự nhiên!")
else:
    soDaoNguoc = 0
    #Su dung vong while de tach cac chu so
    while soBanDau > 0:
        chuSoCuoi = soBanDau % 10
        soDaoNguoc = soDaoNguoc * 10 + chuSoCuoi
        soBanDau //= 10
    print('Số đảo ngược của số',temp, 'là:',soDaoNguoc)
