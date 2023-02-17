n = int(input('Nhập số nguyên dương n: '))
S4 = 0
S5 = 0
S6 = 0
if n<1:
    print('n không hợp lệ, hãy nhập lại n')
else:
    for x in range(1,n+1):
        S4+=x*x
    for y in range(1,2*n+2,2):
        S5+=y*y*y
    for z in range(2,2*n+1,2):
        S6+=z*z*z*z
    print('S4 =',S4)
    print('S5 =',S5)
    print('S6 =',S6)
