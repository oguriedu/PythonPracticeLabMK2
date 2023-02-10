'''Viết chương trình nhập tháng trong năm'''
while True:
    month=["January","February","March","April","May","June","July","August","September","October","November","December"]
    choice=int(input("Nhập tháng(1->12):"))
    if 0<choice<13:
        print(choice,":",month[choice-1])
    else:
        print("Tháng không hợp lệ nhập lại:")