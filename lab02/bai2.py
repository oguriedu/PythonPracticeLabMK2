nhập  toán 
in ( "pt:ax2 + bx + c = 0 (a khác 0)" )
a  =  int ( input ( "nhập hệ số a: " ))
b  =  int ( input ( "nhập hệ số b: " ))
trong khi  Đúng :
    nếu  một  ==  0 :
        print ( "Một trong hai hệ thống số a, b phải khác 0: " )
        a  =  int ( input ( "Mời nhập lại số a: " ))
    khác :
        phá vỡ
c  =  int ( input ( "nhập hệ số c: " ))
đồng bằng  =  b ** 2  -  4  *  a  *  c
nếu  đồng bằng  <  0 :
    print ( "Phương trình vô nghiệm" )
Elif  delta  ==  0 :
    print ( "Phương trình có nghiệm kép x1= x2= " , - ( b  / ( 2  *  a )) )
khác :
    print ( "Phương trình có hai phân biệt:" )
    in ( "x1= " , ( - ( b ) +  math . sqrt ( delta )) / ( 2 * a ) )
    in ( "x1= " , ( - ( b ) -  math . sqrt ( delta )) / ( 2 * a ) )