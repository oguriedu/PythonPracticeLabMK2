t=float(input('nhập thời gian:'))
u=220
i=2.7
A_Ws=u*i*t
A_kWh=A_Ws/(3600*1000)
tien=A_kWh*7000
print('với thời gian sử dụng bóng đèn là',t,'s','tiền điện là:',tien,'đồng')