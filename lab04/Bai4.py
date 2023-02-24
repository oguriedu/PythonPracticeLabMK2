import fractions
a=int(input("Nhap tu so: "))
while True:
   b=int(input("Nhap mau so: "))
   if b>0:
      break
print("Vui long nhap lai")
fraction = fractions.Fraction(a,b)
print(f"Phan so la: {fraction}")
