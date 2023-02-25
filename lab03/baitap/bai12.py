chu=["A","B","C","D","E",'F',"G","H","I","J","k","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
so=[10,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38]
nhap=(input("nhập số của container (4 ký tự đầu là chữ cái,6 số sau là chữ số): "))
l=0
tong_chuso=0
tong_chu=0
for i in nhap:
    if l<=3:
        chu_cai=chu.index(nhap[l])
        chu_so=so[chu_cai]
        tong_chu+=chu_so*(2**l)
    if l>3:
        tong_chuso+=int(i)*(2**(l))
    l+=1
print("số kiểm tra của mã container là: ",(int(tong_chuso)+int(tong_chu))%11)