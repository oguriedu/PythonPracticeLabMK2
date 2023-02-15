chu=["A","B","C","D","E",'f',"G","H","I","J","k","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
so=[10,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38]
h=(input("nhập số của container (4 ký tự đầu là chữ cái,6 số sau là chữ số): "))
chu1=chu.index(h[0])
so1=so[chu1]
chu2=chu.index(h[1])
so2=so[chu2]
chu3=chu.index(h[2])
so3=so[chu3]
chu4=chu.index(h[3])
so4=so[chu4]
chuso=so1*1+so2*2+so3*4+so4*8
l=-1
w=0
for i in h:
    l+=1
    if l>3:
        w+=int(i)*(2**l)
print("số kiểm tra của mã container là: ",(int(w)+int(chuso))%11)
        