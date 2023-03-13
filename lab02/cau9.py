kwuse=float(input('Nhập số KW đã sử dụng :'))
if 0<kwuse<=100:
    tien=kwuse*2000
elif 100<kwuse<=200:
    tien=(100*2000)+((kwuse-100)*2500)
elif 200<kwuse<=300:
    tien=(100*2000)+(100*2500)+((kwuse-200)*3000)
else :
    tien=(100*2000)+(100*2500)+(100*3000)+((kwuse-300)*5000)
print('Tiền điện của b là {:,} VNĐ'.format(int(tien)))