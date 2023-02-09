a={1:'Sunday',2:'Monday',3:'Tuesday',4:'Wednesday',5:'Thursday',6:'Friday',7:'Saturday'}
t=int(input('Nhập thứ trong tuần(1->7): '))
while (t>7)or(t<1):
    print('Mời nhập lại!')
    t=int(input('Nhập thứ trong tuần(1->7): '))
print('Thứ {} tên là {}'.format(t,a.get(t)))
print(t,':',a.get(t))
