#
a = float(input("Nhập số KW : "))
if 0<a<=100:
    print("Số tiền điện là : ",2000*a,'đồng')
elif 101<=a<=200:
    print("Số tiền điện là : ",2500*a,'đồng')
elif 201<=a<=300:
    print("Số tiền điện là : ",3000*a,'đồng')
elif a>300:
    print("Số tiền điện là : ",5000*a,'đồng')