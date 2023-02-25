import math
#a
S = 0 
n = 1 
while n < 5: S += (-1)**(n+1) * (1/n) 
n += 1 
print(S)

#b
S = 0 
n = 2 
while n < 5: S += (1/(n(n+1))) 
n += 1 
print(S)

#c
S = 0 
n = 2 
while n < 5: S += (1/math.sqrt(n)) 
n += 1 
print(S)