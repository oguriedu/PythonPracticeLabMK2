n=int(input('moi nhap mot so: '))
so=["khong","mot","hai","ba","bon","nam","sau","bay","tam","chin"]
in_ra=" "
tach_so=[]
for i in str(n):
    tach_so.append(int(i))
for num in tach_so:
    for j in range(0,len(so)-1):
        if num==j:
            in_ra+=so[j]
            in_ra+=" "
print(in_ra)
