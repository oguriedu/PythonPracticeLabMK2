def ngto(n):
    for i in range(2,int(n**1/2)):
        if n%i==0:
            return False
    return True 
n=int(input("Nhập n: "))
m=n
d1=0
d2=0
if ngto(n)==True:
    print("n là số nguyên tố")
else:
    print(n,"không phải là số nguyên tố")
    while ngto(n)==False:
        n-=1
        d1+=1
    while ngto(m)==False:
        m+=1
        d2+=1 
    if d2>d1:
        print("số nguyên tố gần n nhất là :",n)
    elif d1>d2:
        print("số nguyên tố gần n nhất là :",m)
    elif d1==d2:
        print("số nguyên tố gần n nhất là :",m,"và",n)
        