#bài 2
s = int(input('Nhập giá trị giây:'))
m = int(input('Nhập giá trị phút:'))
h = int(input('Nhập giấ trị giờ:'))
d = int(input('Nhập giá trị ngày:'))
print('Thời gian quy đổi theo ngày là:',round((d+(h/24)+(m/1440)+(s/86400)),2))
print('Thời gian quy đổi theo giờ là:',round(((d*24)+h+(m/60)+(s/3600)),2))
print('Thời gian quy đổi theo phút là:',round(((d*1440)+(h*60)+m+(s/60)),2))
print('Thời gian quy đổi theo giây là:',round(((d*86400)+(h*3600)+(m*60)+s),2))