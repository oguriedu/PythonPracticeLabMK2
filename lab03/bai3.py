a= int(input("nhap so "))
if (a == 1 ) :
    print("không phải là số nguyên tố")
x=a
y=a
for i in range(2,a+1):
     if (a==i):#tức là chia hết cho chính số đó
         print(a,"là số nguyên tố")
     if (a%i==0):#tức là còn có thể chia hết cho những số khác
        print(a,"không phải là số nguyên tố")
        while True:
            x=x+1
            y=y-1
            for i in range(2,x+1):
                if(x==i):
                    print(x,"là số nguyên tố gần",a,'nhất')
                    x=""
                    break
                if (x%i==0):
                    break
            for i in range(2,y+1):
                if(y==i):
                    print(y,"là số nguyên tố gần",a,'nhất')
                    y=""
                    break
                if (y%i==0):
                    break
            if ((x=='')or (y=='')):
                break
        break