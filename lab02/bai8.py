x=float(input('nhập số tháng làm việc:'))
LCB=1350000

if x<12:
       HS=2.34
       
elif x>=12 and x<36:
       HS=3.33
            
elif x>=36 and x<60:
       HS=3.66
else:
      HS=3.99
      
Lương=HS*LCB
print('lương của bạn là: %0.0f'%Lương)