a = input('Nhập số có 3 chữ số: ').split()

if a<100 or a>=1000:
    a = int(input('Nhập lại số có 3 chữ số: '))
    
tram = ['không trăm','một trăm','hai trăm','ba trăm','bốn trăm','năm trăm','sáu trăm','bảy trăm','tám trăm','chín trăm'] 
chuc = ['lẻ','mười','hai mươi','ba mươi','bốn mươi','năm mươi','sáu mươi','bảy mươi','tám mươi','chín mươi']
don_vi = ['không','một','hai','ba','bốn','năm','sáu','bảy','tám','chín']

if a[2]== "0" and a[1]=="0":
    print(tram[int(a[0])])
elif a[2]=="0":
    print(tram[int(a[0])],chuc[int(a[1])])
else :
    print(tram[int(a[0])],chuc[int(a[1])],don_vi[int(a[2])])