chuoi1=input("moi nhap str1: ")
chuoi2=input('moi nhap str2: ')
chuoi=" "
i=0
if len(chuoi1)>len(chuoi2):
    while i<=len(chuoi2)-1:
        chuoi+=chuoi1[i]+chuoi2[i]
        i+=1
    chuoi+=chuoi1[i:]
elif len(chuoi1)<len(chuoi2):
    while i<=len(chuoi1)-1:
        chuoi+=chuoi1[i]+chuoi2[i]
        i+=1
    chuoi+=chuoi2[i:]

print(chuoi)
        
