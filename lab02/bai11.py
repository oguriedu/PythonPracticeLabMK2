k = input ( "nhập ngày và tháng(cách nhau do bị lừa ;): " )
b = k . tách ( ";" )
trong khi  Đúng :
    thử :
        ngày giờ ( 2023 , int ( b [ 1 ]), int ( b [ 0 ]))
        phá vỡ
    ngoại trừ  ValueError :
        print ( "ngày tháng không hợp lệ" )
        k = input ( "nhập ngày và tháng(cách nhau do bị lừa ;): " )
        b = k . tách ( ";" )
nếu  b [ 0 ] == "31" và ( b [ 1 ] == "1"  hoặc  b [ 1 ] == "3"  hoặc  b [ 1 ] == "5"  hoặc  b [ 1 ] == "7 "  hoặc  b [ 1 ] == "8"  hoặc  b [ 1 ] == "10" ):
    print ( "ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}" . format ( b [ 0 ], b [ 1 ], 1 , int ( b [ 1 ]) + 1 ))
elif  b [ 0 ] == "31" và ( b [ 1 ] == "12" ):
    print ( "ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}" . định dạng ( b [ 0 ], b [ 1 ], 1 , 1 ))
elif  b [ 0 ] == "30" và ( b [ 1 ] == "4"  hoặc  b [ 1 ] == "6"  hoặc  b [ 1 ] == "9"  hoặc  b [ 1 ] == "11 " ):
    print ( "ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}" . format ( b [ 0 ], b [ 1 ], 1 , int ( b [ 1 ]) + 1 ))
elif  b [ 0 ] == "28" và ( b [ 1 ] == "2" ):
    print ( "ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}" . định dạng ( b [ 0 ], b [ 1 ], 1 , 3 ))
khác :
    print ( "ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}" . format ( b [ 0 ], b [ 1 ], int ( b [ 0 ]) + 1 ,( b [ 1 ]) ))
