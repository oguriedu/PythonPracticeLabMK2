a=input("nhập số nguyên: ")
if int(a) <100:
    print("chữ số hàng trăm của số {} là {}".format(a,0))
else:
   print("chữ số hàng trăm của số {} là {}".format(a,a[len(a)-3]))
