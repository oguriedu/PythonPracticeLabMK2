s4 = 0
s5 = 0
s6 = 0
n = int(input('Nhập n: '))
while n<=0:
    n = int(input('Nhập lại n: '))
    break
for i in range(1,n+1):
    s4+=i*i
    if i%2!=0:
        s5+=i**3
    elif i%2==0:
        s6+=i**4
print(s4)
print(s5)
print(s6)