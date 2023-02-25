n=int(input("Nhập số nguyên dương: "))
s4=0
s5=0
s6=0
while n<=0:
     print("Nhập sai, số n phải lớn hơn 0. Nhập lại")
     n=int(input("Nhập số nguyên dương: "))
for i in range(n):
          k4=i**2
          k5=(2*i+1)**3
          k6=(2*i)**4
          s4+=k4
          s5+=k5
          s6+=k5    
print('Tổng của n số nguyên dương 4 là',s4)
print('Tổng của n số nguyên dương 5 là',s5)
print('Tổng của n số nguyên dương 6 là',s6)

    