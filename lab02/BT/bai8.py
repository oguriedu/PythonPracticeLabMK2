a=float(input("nhập số tháng công tác: "))
t=1350000
if a<12:
    t=t*2.34
elif a<36:
    t=t*3.33
elif a<60:
    t=t*3.66
else:
    t=t*3.99
print("lương của bạn là",t)
