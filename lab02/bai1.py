a = float(input("nhập tháng cần biết(t1-t12):"))
if (a==10)or(a==3)or(a==5)or(a==7)or(a==8)or(a==10)or(a==12):
    print(a,"là tháng có 31 ngày")
elif (a==4)or(a==6)or(a==9)or(a==11):
    print(a,"là tháng có 30 ngày")
else :
    print(a,"là tháng có 28 ngày")   
