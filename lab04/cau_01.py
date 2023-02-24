s4 = 0
s5 = 1
s6 = 0

while True:
    n = int(input("Nhap so nguyen to N: "))
    if (n > 0):
       for i in range (1, n+1):
           s4 += i**2
           s5 += (2*i+1)**3
           s6 += (2*i)**4
       print("Tong dau tien la:",s4,"\n","Tong thu hai la:",s5,"\n","Tong thu ba la:",s6)      
       break
  

