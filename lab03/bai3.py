n = int(input("hãy nhập số n : "))
flag = True
for i in range(2,n):
    if (n%i ==0):
        flag= False

if (flag == False):
    print(n, " không phải số nguyên  tố")
else:
    for i in range (1,n):
        t = n -i
        print (t)
    
        

