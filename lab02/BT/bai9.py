a=int(input("nhap so kw "))
if(a<=100):
     a= a*2000
elif(a<=200):
     a= (a-100)*2500+100*2000
elif(a<=300):
     a= (a-200)*3000+200*2500+100*2000
else:
     a= (a-300)*5000+300*3000+200*2500+100*2000
print("so tien phai tra",a)
