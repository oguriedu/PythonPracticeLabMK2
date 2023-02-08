x=float(input("Nhập số KW : "))
if 0<x<=100:
    print("Số tiền điện là : ",2000*x,'đồng')
elif 101<=x<=200:
    print("Số tiền điện là : ",2500*x,'đồng')
elif 201<=x<=300:
    print("Số tiền điện là : ",3000*x,'đồng')
elif x>300:
    print("Số tiền điện là : ",5000*x,'đồng')