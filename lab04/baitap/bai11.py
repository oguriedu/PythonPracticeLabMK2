do_uong={1:"Cafe",2:"Cam vắt",3:"nước ép cà rốt",4:"nước lọc",5:"nước dừa"}
for i in do_uong:
    print(i,":",do_uong[i])
muon=int(input("ban muon uong gi? "))
while True:
    if muon<=0 or muon>5:
        print('trong menu khong co nuoc ban nhap')
        muon=int(input('moi ban nhap lai:  '))
    if muon>0 and muon<=5:
        break
print(f"ban da dat {muon}","la",do_uong[muon])