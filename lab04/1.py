
n = int(input("Nhập n là số nguyên dương: "))
while n <= 0:
 print("Vui lòng nhập lại số nguyên dương!")
 n = int(input("Nhập n là số nguyên dương: "))
s4 = 0
i4 = 1
#5
while i4 <= n:
    s4 = s4 + i4**2
    i4 = i4 + 1
print("S4 = 1^2 + 2^2 + 3^2 + ... + n^2 =", s4)
#
s5=0
i5=1
while i5 <= n:
    if i5%2!=0:
        s5=s5+ i5**3
        i5=i5+2
print("S5= 1^3 + 3^3 + 5^3 + ... +(2n+1)^3 =",s5)        
#
s6=0
i6=1
while i6 <= n:
        s6+=i6**4
        i6+=2
print("S6 = 2^4 + 4^4 + 6^4 + … + (2n)^4 =",s6)        
