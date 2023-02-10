nhap=int(input('mời nhập vào số nguyên: '))
hangtram=(nhap%1000)//100
if nhap<100 :
    print(0)
else:
    print("chữ số hàng trăm là: ",hangtram)
    