n=int(input('Nhập vào số nguyên dương:'))
dem=0
for i in range(1,n+1):
    if n % i ==0:
        dem+=1
if dem==2:
        print(n,'Là số nguyên tố')
        print(True)        
else:
        print(n,'Không là số nguyên tố')
        print(False)
for i in range(2,n):
    if n==True:
        print(n, end=" ")