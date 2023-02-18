lstsnt=[]
def Kiem_tra_so_nguyen_to(n):
    flag = 1
    if (n <2):
        flag = 0
        return flag  
    for p in range(2, n):
        if n % p == 0:
            flag = 0
            break
    return flag

n = int(input(" nhap mot so n: "))
for i in range(n):
    check = Kiem_tra_so_nguyen_to(i)
    if( check == 1 ) :
        lstsnt.append(i)
print(max(lstsnt))