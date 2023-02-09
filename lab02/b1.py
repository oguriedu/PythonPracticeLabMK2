'Các tháng 1, 3, 5, 7, 8, 10, 12 có 31 ngày'
'Các tháng 4, 6, 9, 11 có 30 ngày'
'Nếu là tháng 2 thì yêu cầu nhập thêm năm, nếu là năm nhuận thì tháng 2 có 29 ngày, còn lại là 28 ngày. Năm nhuận là năm chia hết cho 4.'
t=int(input('nhập tháng:'))
if t>=1 and t<=12:
    if t==1 or t==3 or t==5 or t==7 or t==8 or t==10 or t==12:
        print('tháng',t,'có 31 ngày')
    if t==4 or t==6 or t==9 or t==11 :
       print('tháng',t,'có 30 ngày')
    if t==2:
       n=eval(input('nhập năm:'))
       if n%4==0:
           print('tháng',t,'có 29 ngày')
       else:
           print('tháng 2 có 28 ngày')
else:
       print('định dạng đầu vào kh hợp lý')
        
           
           
       