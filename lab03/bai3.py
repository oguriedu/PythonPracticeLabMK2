a= int(input("nhap so "))
h=a
m=a
if (a == 1 ) :
    print("không phải là số nguyên tố")
for i in range(2,a+1):
     if(a==i):
         print(a,"là số nguyên tố")
         break
     if (a%i==0):
         print(a,"không phải là số nguyên tố")
         while True:
            h-=1
            m+=1
            for i in range(2,h+1):
                if(h==i):
                    print(h,"là số nguyên tố gần",a,'nhất')
                    h='x'
                    break
                if (h%i==0):
                    break
            for i in range(2,m+1):
                if(m==i):
                    print(m,"là số nguyên tố gần",a,'nhất')
                    m='x'
                    break
                if (m%i==0):
                    break
            if ((h=='x')or (m=='x')):
                break
         break
                    
