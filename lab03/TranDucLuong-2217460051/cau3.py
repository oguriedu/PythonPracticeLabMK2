n=int(input('Enter interger:'))
list=[]
flag= 1
def kiem_tra_snt(n):
    for i in range(2,n):
        if n%i==0:
            flag== 0 
            break
        return flag
for c in range(n+1):
    check=kiem_tra_snt(c)
    if check ==1:
        list.append(c)

a=max(list)
if a==n:
    print (n,'là số nguyên tố ')
else :
    print(a,'là số nguyên tố gần',n,'nhất')

    


