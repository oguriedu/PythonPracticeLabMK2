n = int(input("nhập n = "))
sum = 0
i = 0
sum_bac3 = 0
sum_bac4 = 0
while n <= 0:
    print("bạn nhập sai rồi mời bạn nhập lại")
    n = int(input("nhập n = "))
else:
    while i <= n-1:
        k = 2*i +1
        i += 1
        h = 2*i
        sum += i**2
        sum_bac3 += k**3
        sum_bac4 = h**4
    print("S4 =",sum)
    print("S5 =",sum_bac3)
    print("S6 =",sum_bac4)
