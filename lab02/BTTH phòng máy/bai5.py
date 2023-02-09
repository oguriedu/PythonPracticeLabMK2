def xacdinh(t):
    if t==1:
        print("1: January")
    if t==2:
        print("2: February")
    if t==3:
        print("3: March")
    if t==4:
        print("4: April")
    if t==5:
        print("5: May")
    if t==6:
        print("6: June")
    if t==7:
        print("7: July")
    if t==8:
        print("8: August")
    if t==9:
        print("9: September")
    if t==10:
        print("10: October")
    if t==11:
        print("11:November")
    if t==12:
        print("12: December")
while True:
    t=int(input("Nhập tháng trong năm: "))
    if t<1 or t>12:
        print("Mời bạn nhập lại!")
    else:
        xacdinh(t)
        break