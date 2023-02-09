a = input ( "nhập số nguyên: " )
nếu  int ( a ) < 100 :
    print ( " Chữ số hàng phần trăm của số {} là {}" . định dạng ( a , 0 ))
khác :
   print ( " Chữ số hàng phần trăm của số {} là {}" . format ( a , a [ len ( a ) - 3 ]))
