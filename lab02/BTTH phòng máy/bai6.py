def hangtram(tram):
        if tram==1:print('Một')
        if tram==2:print('Hai') 
        if tram==3:print('Ba')
        if tram==4:print('Bốn')
        if tram==5:print('Năm')
        if tram==6:print('Sáu')
        if tram==7:print('Bảy')
        if tram==8:print('Tám')
        if tram==8:print('Chín')
        print('trăm')
def hangchuc(chuc):
    if chuc==1:print('mười')
    if chuc==0:print('linh')
    else:
            if chuc==2:print('hai')
            if chuc==3:print('ba')
            if chuc==4:print('bốn')
            if chuc==5:print('năm')
            if chuc==6:print('sáu')
            if chuc==7:print('bảy')
            if chuc==8:print('tám')
            if chuc==9:print('chín')
            print('Mươi')
def hangdv(dv):
        if dv==1:print('mốt')
        if dv==2:print('hai')
        if dv==3:print('ba')
        if dv==4:print('bốn')
        if dv==5:print('lăm')
        if dv==6:print('sáu')
        if dv==7:print('bảy')
        if dv==8:print('tám')
        if dv==9:print('chín')
while True:
    a=int(input("Nhập số nguyên: "))
    if a<100 or a>999:
        print("Mời bạn nhập lại!")
    else:
        dv=(a%100)%10                                                        
        chuc=(a%100)//10
        tram=a//100
        hangtram(tram)
        hangchuc(chuc)
        hangdv(dv)
        break

        

        
