ts=float(input('Nhập thời gian sử dụng bóng đèn (giây): '))
U=220
I=2.7
P=U*I*0.001 #Tính công suất tiêu thụ(kW)
th=ts*0.00027777777777778 #Đổi thời gian sử dụng từ s sang h
A=P*th #Tính điện năg tiêu thụ(kWh)
tdien=A*7000 #Tính tiền điện
print('Tiền điện phải trả: ',tdien,'vnđ')