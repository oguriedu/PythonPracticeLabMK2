while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n > 0:
        break
    else:
        print("Số n phải là một số nguyên dương. Vui lòng nhập lại.")
        
# tính tổng S4
S4 = 0
for i in range(1, n+1):
    S4 += i**2
    
print("Tổng S4 = ", S4)

# tính tổng S5
S5 = 0
for i in range(0, n+1):
    S5 += (2*i+1)**3
    
print("Tổng S5 = ", S5)

# tính tổng S6
S6 = 0
for i in range(1, n+1):
    S6 += (2*i)**4
    
print("Tổng S6 = ", S6)
