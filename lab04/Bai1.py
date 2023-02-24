while True:  
    n= int(input("Nhập số nguyên dương n: "))
    if n>0:
      break
    print("Vui long nhap lai")
S4 = 0
S5 = 0
S6 = 0
i=1
while i <=n:
    S4 += i**2
    i += 1
print("tong day so :", S4)
i=1
while i<= 2*n+1:
   S5 += i**3
   i += 2
print("tong day so: ",S5)
i=2
while i <=2*n:
   S6 += i ** 4
   i+=2
print("Tong day so: ",S6)
