chu=["A","B","C","D","E",'f',"G","H","I","J","k","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
so=[10,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38]
h=(input("nhập số của container (4 ký tự đầu là chữ cái,6 số sau là chữ số): "))
l=0
w=0
w1=0
for i in h:
    if l<=3:
        chu1=chu.index(h[l])
        so1=so[chu1]
        w1+=so1*(2**l)
    if l>3:
        w+=int(i)*(2**(l))
    l+=1
print("số kiểm tra của mã container là: ",(int(w)+int(w1))%11)
        