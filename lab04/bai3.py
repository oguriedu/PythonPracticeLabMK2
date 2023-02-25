#
n=int(input('nhập số n: '))
x=int(input('nhập số x: '))
while True:
    if n<=0:
        n=int(input("hãy nhập lại n cho đúng: "))
    if n>0:
        break
#tinh giai thua
def giai_thua(n):
    giai_thua = 1
    if (n == 0 or n == 1):
        return giai_thua
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i
        return giai_thua
cos=1
k=1
for i in range(1,n+1):
    cos+=(((-1)**k)*(x**(2*i)))/giai_thua(2*i)
    k+=1
print(cos)