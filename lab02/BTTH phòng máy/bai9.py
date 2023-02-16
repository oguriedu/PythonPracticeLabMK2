x=float(input("Nhập số KW:"))
if 0<x<=100:
    print("Số tiền phải trả là:",2000*x)
elif 101<=x<=200:
    print("Số tiền điện là:",2500*x)
elif 201<=x<=300:
    print("Số tiền điện là:",3000*x)
elif x>300:
    print("Số tiền điện là:",5000*x)