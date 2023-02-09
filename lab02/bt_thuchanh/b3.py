def xacdinh(t):
    if t==1:
        print("1:SUNDAY")
    elif t==2:
        print("2:MONDAY")
    elif t==3:
        print("3:TUESDAY")
    elif t==4:  
        print("4:WESNESDAY")
    elif t==5:
        print("5:THURSDAY")
    elif t==6:
        print("6:FRIDAY")
    elif t==7:
        print("7:SATURDAY")
while True:
    t=int(input("Nhập thứ trong tuần: "))
    if t<1 or t>7:
        print("Mời bạn nhập lại!")
    else:
        xacdinh(t)
        break
