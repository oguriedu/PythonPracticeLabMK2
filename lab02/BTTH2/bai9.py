a = float(input("Nhập số KW : "))
if 0<a<=100:
    print("Số tiền điện là : ",2000*a,'đồng')
elif 101<=a<=200:
    print("Số tiền điện là : ",2000*100+(a-100)*2500,'đồng')
elif 201<=a<=300:
    print("Số tiền điện là : ",2000*100+2500*100+(a-200)*3000,'đồng')
elif a>300:
    print("Số tiền điện là : ",2000*100+2500*100+100*3000+(a-300)*5000,'đồng')