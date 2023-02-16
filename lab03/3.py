a= int(input("Nhập một số:"))
b= True
if (a<2):
    b= False
for i in range (2,a):
    if (a%i==0):
        b= False
    if b:
        print(a, "là số nguyên tố" )
    else:
        print(a, "không phải là số nguyên tố")           
