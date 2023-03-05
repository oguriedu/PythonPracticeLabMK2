a=input('moi nhap so: ')
b=input('moi nhap so: ')
a_so=''
b_so=''
for i in a:
    if i.isnumeric()==True:
        a_so+=i
for j in b:
    if j.isnumeric()==True:
        b_so+=j
for k in range(1,len(a_so)):
    for l in range(1,len(b_so)):
        so=a_so[:k]
        so1=a_so[k:]
        kiem_tra=int(so)+int(so1)
        so3=b_so[:l]
        so4=b_so[l:]
        kiem_tra1=int(so3)+int(so4)
        if kiem_tra==kiem_tra1:
            print(f"{so}+{so1}={so3}+{so4}")
if kiem_tra!=kiem_tra1:
        print("khong ton tai cach dat")
        

    