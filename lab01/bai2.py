#viết công thức đổi giá trị
s=int(input('Nhập số giây: '))
m=int(input("Nhập số phút: "))
h=int(input('Nhập số giờ: '))
d=int(input('Nhập số ngày: '))
print("{}ngày,{}giờ,{}phút,{}giây".format(d,h,m,s),"bằng",round(d+(h/24)+(m/1440)+(s/86400),2),"ngày")
print("{}ngày,{}giờ,{}phút,{}giây".format(d,h,m,s),"bằng",round((d*24)+h+(m/60)+(s/3600),2),"giờ")
print("{}ngày,{}giờ,{}phút,{}giây".format(d,h,m,s),"bằng",round((d*1440)+(h*60)+m+(s/60),2),"phút")
print("{}ngày,{}giờ,{}phút,{}giây".format(d,h,m,s),"bằng",round(s+(m*24)+(h*1440)+(d*86400),2),"giây")