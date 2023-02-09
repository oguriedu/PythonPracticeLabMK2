a = input ( "Nhập tốc độ A(x,y phân cách theo dấu ';'): " )
b = input ( "Nhập tốc độ B(x,y phân cách theo dấu ';'): " )
tda = a . tách ( ";" )
tdb = b . tách ( ";" )
t = 0
cho  tôi  trong  phạm vi ( len ( tda )):
    t += int ( tda [ i - 1 ]) * int ( tdb [ i - 1 ])
print ( "ích vô hướng của A và B: " , t )