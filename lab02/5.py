#5
n = int(input('Nhập tháng: '))
while n>=12 and n<0:
    n = int(input('Nhập lại tháng: '))
    break
thang = ['1:January','2:February','3:March','4:April','5:May','6:June','7:July','8:August','9:September','10:October','11:November','12December']
n = n-1
print(thang[n])