print ( "khung giờ từ 5h đến 22h" )
k = input ( "nhập giờ bắt đầu và kết thúc(cách nhau do lừa; sân: " )
b = k . tách ( ";" )
trong khi ( int ( b [ 0 ]) < 5 ) hoặc ( int ( b [ 0 ]) > 22 ):
    print ( "khung giờ không hợp lệ" )
    k = input ( "nhập giờ bắt đầu và kết thúc(cách nhau do lừa; sân: " )
a = int ( b [ 1 ]) - int ( b [ 0 ])
nếu ( a <= 3 ):
     một =  một * 100000
yêu tinh ( a <= 11 ):
     a = ( a - 3 ) * 75000 + 300000
yêu tinh ( a <= 15 ):
     a = (((( a - 3 ) * 75000 + 300000 ) * 90 ) / 100 )
khác :
     a = ( a - 3 ) * 75000 + 300000
print ( "số tiền phải trả" , a )