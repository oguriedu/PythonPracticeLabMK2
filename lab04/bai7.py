a = int ( input ( "nhập a: " ))
b = int ( input ( "nhập b: " ))
nếu  a >= b :
     c = một
khác :
     c = b
nếu ( a == b ) hoặc ( a % b == 0 ) hoặc ( b % a == 0 ):
     print ( c , "là bội chung nhỏ nhất" )
trong khi ( c % a != 0 ) hoặc ( c % b != 0 ):
     c += 1
     nếu ( c % a == 0 ) và ( c % b == 0 ):
         print ( c , "là bội chung nhỏ nhất" )
         phá vỡ