ts=float(input('Nhập thời gian sử dụng bóng đèn (giây): '))
U=220
I=2.7
#Tính công suất tiêu thụ(kW)
P=U*I*0.001
#Đổi thời gian sử dụng từ s sang h
th=ts*0.00027777777777778
#Tính điện năg tiêu thụ(kWh)
A=P*th
#Tính tiền điện
tdien=A*7000
print('Tiền điện phải trả: ',tdien,'vnđ')
