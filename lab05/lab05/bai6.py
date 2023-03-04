chuoi=input("moi nhap chuoi: ")
chu=["A","B","C","D","E","F"]
thap_phan=" "
for i in chuoi:
    kiem_tra=i.isalpha()
    if i.isnumeric()==True:
        thap_phan+=str(i)
thap=int(thap_phan)
in_ra=" "
while thap!=0:
    thap_nhi=thap%16
    if thap_nhi>=10:
        in_ra+=chu[thap_nhi%10]
    else:
        in_ra+=str(thap_nhi)
    in_ra+=" "
    thap=(thap-thap_nhi)//16
print("".join(list(reversed(in_ra.split()))))


