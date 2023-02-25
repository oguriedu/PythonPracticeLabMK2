nhập hệ  điều hành
print ( ' \n MENU ĐỒ UỐNG Ở "TIỆM NHỎ CỦA TỚ" ' )
trong khi  Đúng :
    in ( ' _________________________ ' )
    print ( '| Menu select đồ uống |' )
    in ( '| [1] Quán cà phê |' )
    print ( '| [2] Cam vắt |' )
    print ( '| [3] Nước ép cà rốt |' )
    print ( '| [4] Water filter |' )
    print ( '| [5] Nước dừa |' )
    print ( '| [0] Bấm 0 để thoát |' )
    in ( '|____________________________________|' )

    chon  =  int ( input ( 'chọn đồ uống mà bạn muốn: ' ))
    nếu  chơn  ==  1 :
        print ( 'xin đợi một lát, chúng tôi sẽ phục vụ quán cà phê cho bạn.' )
    elif  chơn  ==  2 :
        print ( 'xin đợi một lát, chúng tôi sẽ phục vụ Cam vắt cho bạn.' )
    elif  chơn  ==  3 :
        print ( 'xin đợi một lát, tôi sẽ phục vụ Nước ép cà rốt cho bạn.' )
    elif  chơn  ==  4 :
        print ( 'xin đợi một lát, chúng tôi sẽ phục vụ Bộ lọc nước cho bạn.' )
    elif  chơn  ==  5 :
        print ( 'xin đợi một lát, tôi sẽ phục vụ Nước dừa cho bạn.' )
    elif  chơn  ==  0 :
        phá vỡ
    khác :
        print ( 'chỉ chọn các số từ 1 đến 5' )
    tt  =  input ( 'nhấn phím bất kỳ để tiếp tục (bấm 0 để thoát): ' )
    nếu  tt  ==  '0' :
        phá vỡ
    khác :
        hệ điều hành . hệ thống ( 'cls' )