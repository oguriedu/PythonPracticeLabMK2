
n = int(input("Please enter a positive integer: "))

while n <= 0: n = int(input("Please enter a positive integer: "))

s4 = 0 
s5 = 0 
s6 = 0

for i in range (1, n+1): s4 = s4 + i**2

for i in range (1, n+1): s5 = s5 + (2*i+1)**3

for i in range (1, n+1): s6 = s6 + (2*i)**4

print("S4 =", s4) 
print("S5 =", s5) 
print("S6 =", s6)