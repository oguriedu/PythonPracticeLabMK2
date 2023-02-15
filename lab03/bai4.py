a= int(input("nhập s: "))
for k in range(2,a+1):
    for i in range(2,k+1):
        if(k==i):
            print(k,"là số nguyên tố ")
            break
        if (k%i==0):
            break