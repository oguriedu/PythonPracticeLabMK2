n = int(input('Nhập ngày: '))
t = int(input('Nhập tháng: '))
while (n==31)and(t==4 or t==6 or t==9 or t==11 ):
    print('Ngày tháng không hợp lệ mời nhập lại ! ')
    n = int(input('Nhập ngày: '))
    t = int(input('Nhập tháng: '))
if n==30 and (t==4 or t==6 or t==9 or t==11 ):
    print('Ngày tiếp theo của ngày {}/{} là ngày {}/{}'.format(n,t,1,t+1))
elif n==31 and (t==1 or t==3 or t==5 or t==7 or t==8 or t==10 or t==12 ):
    print('Ngày tiếp theo của ngày {}/{} là ngày {}/{}'.format(n,t,1,t+1))   
elif n==31 and t==12:
    print('Ngày tiếp theo của ngày {}/{} là ngày {}/{}'.format(n,t,1,1))
elif t==2 and n==28 :
    print('Ngày tiếp theo của ngày {}/{} là ngày {}/{}'.format(n,t,1,t+1))
else:
    print('Ngày tiếp theo của ngày {}/{} là ngày {}/{}'.format(n,t,n+1,t))
