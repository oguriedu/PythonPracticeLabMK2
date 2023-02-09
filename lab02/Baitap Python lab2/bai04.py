number=int(input("nhập vào một số nguyên :"))
if number < 100 :
    print(0)
else :
    b=(number%1000)//100
    print("chữ số hàng trăm của số là :",b)