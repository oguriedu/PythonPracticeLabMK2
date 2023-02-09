a = input ( "nhập đỉnh A(x và y phân cách theo dấu ';'): " )
b = input ( "nhập đỉnh B(x và y phân cách theo dấu ';'): " )
c = input ( "nhập đỉnh C(x và y phân cách do bị khóa ';'): " )
tda = a . tách ( ";" )
tdb = b . tách ( ";" )
tdc = c . tách ( ";" )
h = []
cho  tôi  trong  phạm vi ( len ( tda )):
    m = ( int ( tda [ i ]) + int ( tdb [ i ]) + int ( tdc [ i ]) / 3 )
    h . nối thêm ( m )
print ( "tọa độ trọng tâm của tam giác ABC là" , h )
