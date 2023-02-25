n= int(input("nhập số nguyên dương n:"))
if n<0:
    print ("Vui lòng nhập lại n:")

s=0
for i in range (1, n+1):
    s+=i**2
    print ("S4= 1^2+ 2^2+ 3^2+...+n^2 =", s)

for i in range (1, n+1, 2):
    if i%2!=0:
        s+=i**3
    print ("S5= 1^3+ 3^3+ 5^3+...+(2n+1)^3 =",s)


