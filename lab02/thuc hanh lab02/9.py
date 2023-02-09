w=int(input("nhap so kw "))
if(w<=100):
     w= w*2000
elif(w<=200):
     w= (w-100)*2500+100*2000
elif(w<=300):
     w= (w-200)*3000+200*2500+100*2000
else:
     w= (w-300)*5000+300*3000+200*2500+100*2000
print("so tien phai tra",w)
