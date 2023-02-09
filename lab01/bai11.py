a = int ( input ( 'Nhập số lần tung xúc sắc: ' ))
xs  =  1 - ( 215 / 216 ) ** a
print ( 'xác suất khi tung {} lần 3 cảm sắc có ít nhất 1 lần cả 3 ra 6 là {} %' . format ( a , round ( xs * 100 , 2 )))
