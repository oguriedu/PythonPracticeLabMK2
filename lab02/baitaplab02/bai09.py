a=int(input("Nhập số KW : "))
if(a<=100):
     a= a*2000
elif(a<=200):
     a= 100*2000+(a-100)*2500
elif(a<=300):
     a= 100*2000+100*2500+(a-200)*3000
else:
     a= 100*2000+100*2500+100*3000+(a-300)*5000
print("Tiền điện :",a,'đồng')