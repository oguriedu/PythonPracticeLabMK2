#chương trình in ra cách đọc của số có 3 chữ số:
x=int(input("nhập số có 3 chữ số bạn cần đọc : "))
a=(x//100)
b=(x-(a*100))//10
c=x-(a*100+b*10)
if x>=100 and x<=999:
    print("Đọc số ",x,"là : ",a,"trăm",b,"chục",c,"đơn vị")
else:
    print("bạn đã  nhập sai số ,hãy nhập lại ")