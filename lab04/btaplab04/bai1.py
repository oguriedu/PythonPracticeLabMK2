n=int(input("Nhập số nguyên dương n:"))
s4=0
s5=0
s6=0
i=1
while n<=0:
    n=int(input("Mời bạn nhập lại:"))
while i<=n:
     s4=i**2
     s5=(2*i+1)**3
     s6=(2*i)**4
     i=i+1
print("Tổng của s4 là:",s4)
print("Tổng của s5 là:",s5)
print("Tổng của s6 là:",s6)


