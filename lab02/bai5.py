#
a={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',
8:'August',9:'Septemper',10:'October',11:'November',12:'December'}
t=int(input("Nhập tháng trong năm(1->12): "))
while (t>12)or(t<1):
    print('Mời nhập lại!')
    t=int(input("Nhập tháng trong năm(1->12): "))
print('Tháng {} tên là {}'.format(t,a.get(t)))
print(t,':',a.get(t))