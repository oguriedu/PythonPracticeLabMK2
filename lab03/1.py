tong = 1
n = 1
print('nhập số n:')
n=int(input())
for i in range(0,n+1):
    tong += 2*(i+1)/(2*i+3)
print(f"tổng số là {tong:.3f}")