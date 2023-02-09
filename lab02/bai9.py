a = int ( input ( "nhap so kw " ))
nếu ( a <= 100 ):
     một =  một * 2000
yêu tinh ( a <= 200 ):
     a = ( a - 100 ) * 2500 + 100 * 2000
yêu tinh ( a <= 300 ):
     a = ( a - 200 ) * 3000 + 200 * 2500 + 100 * 2000
khác :
     a = ( a - 300 ) * 5000 + 300 * 3000 + 200 * 2500 + 100 * 2000
print ( "so tien phai tra" , a )
