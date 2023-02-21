n = int(input("Please enter a positive integer: ")) 
while n <= 0: n = int(input("The input must be a positive integer. Please try again: "))

#a 
S1 = 0 
for i in range(1,n+1): S1 += i 
S1 = S1 * (n+1) / 2

#b
S2 = 0 
for i in range(1, (2*n+1), 2): S2 += i 
S2 = (n+1)**2

#c
S3 = 0 
for i in range(2, (2*n+1), 2): S3 += i 
S3 = n * (n+1)

print("S1 =", S1)
print("S2 =", S2) 
print("S3 =", S3)