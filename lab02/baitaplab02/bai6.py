x=int(input('Nhập số nguyên có 3 chữ số: '))
m={0:'linh',1:'một',2:'hai',3:'ba',4:'bốn',5:'năm',6:'sáu',7:'bảy',8:'tám',9:'chín'}
a=x//100
b=(x-a*100)//10
c=(x-a*100)%10
if (b==0)&(c==0):
    print('Số {} đọc là {} trăm'.format(x,m.get(a)))
elif (b==0)&(c!=0):
    print('Số {} đọc là {} trăm linh {}'.format(x,m.get(a),m.get(c)))
elif (b!=0)&(c==0)&(b!=1):
    print('Số {} đọc là {} trăm {} mươi'.format(x,m.get(a),m.get(b)))
elif (b==1):
    print('Số {} đọc là {} trăm mười'.format(x,m.get(a)))
else:
    print('Số {} đọc là {} trăm {} mươi {}'.format(x,m.get(a),m.get(b),m.get(c)))
    