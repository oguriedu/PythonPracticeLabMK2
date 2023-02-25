n=int(input("nhập số nguyên dương n:"))
while n<=0:
    print ("nhập lại n:")
    break
S4=0
S5=0
S6=0
i=0
#S4
while i<= n:
    S4+=i**2
    i+=1
    print("tổng S4 là:",S4)
