n= int(input("nhập số n:"))
a= True
if (n<2):
    a= False
for i in range (2,n):
    if (n%i==0):
        a= False
    if a:
        print(n, "là số nguyên tố" )
    else:
        print(n, "không phải là số nguyên tố")           
