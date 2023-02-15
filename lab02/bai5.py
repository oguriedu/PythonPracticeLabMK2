t = int(input('Nhập tháng: '))
while t>=12 and t<0:
    t = int(input('Nhập lại tháng: '))
    break
thang = ['January ',['February'],'March',['April'],'May','June','July','August','September','October','November','December']
t = t-1
print(thang[t])