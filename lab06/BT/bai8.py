def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)
n=int(input("Nhập số n: "))
a = []
for x in range(0, n+1):
    a.append(str(f(x)))    
print (",".join(a))