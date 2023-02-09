k=int(input("nhập số giây:"))
day=k//86400
h=(k%86400)//3600
m=((k%86400)%3600)//60
s=((k%86400)%3600)%60
print(day,"ngày",h,"giờ",m,"phút",s,"giây")
