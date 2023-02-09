a = ( input ( "nhập số nguyên có ba chữ số: " ))
trong khi ( int ( a ) < 100 ) hoặc ( int ( a ) >= 1000 ):
    print ( ) _
    a = input ( "vui lòng nhập lại: " )
tram = [ "không trăm" , "một trăm" , "hai trăm" , "ba trăm" , "bốn trăm" , "năm trăm" , "sáu trăm" , "bảy trăm" , "tám trăm" , "chín trăm" ]
chuc = [ "lẻ" , "mười" , "hai muơi" , "ba muội" , "bốn muội" , "năm muội" , "sáu muội" , "bảy muội" , "tám muội" , "chín muội" ]
dv = [ "không" , "một" , "hai" , "ba" , "tư" , "năm" , "sáu" , "bảy" , "tám" , "chín" ]

nếu  a [ 2 ] ==  "0"  và  a [ 1 ] == "0" :
    in ( tram [ int ( a [ 0 ])])
elif  a [ 2 ] == "0" :
    in ( tram [ int ( a [ 0 ])], chuc [ int ( a [ 1 ])])
khác :
    print ( tram [ int ( a [ 0 ])], chuc [ int ( a [ 1 ])], dv [ int ( a [ 2 ])])