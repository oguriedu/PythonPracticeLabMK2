def so_nguyen_to(n):
    flag=1
    if n<2:
        flag=0
        return flag
    for i in range(2,n):
        if n%i==0:
            flag=0
            break
    return flag
            
            
#kiem tra
n=int(input("mời nhập n: "))
check=so_nguyen_to(n)
if check==1:
    print(n,'là số nguyên tố')
else:
    print(n,"không là số nguyên tố")
    for j in range(2,n):
        n-=1
        j=n
        check2=so_nguyen_to(j)
        if check2==1:
            print(j)
            break
        
            