n = int(input("Nhập số nguyên dương n: "))
sum = 0 
j = 1
for i in range(0,n):
    k=((2*(i+1))/(2*i+3))
    j=j*k
    print(k,j)
    sum+=j
print(sum+1)
