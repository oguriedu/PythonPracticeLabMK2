s=int(input('Nhập số giây:'))
#công suất tiêu thụ p=U*I
u=220
i=2.7
p=u*i
#điện năng tiêu thụ a=p*t(Kwh)
h=s/3600
a=p*h
#Tiền điện m=a*7000
m=a*7000
print(m)
