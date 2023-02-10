'''Viết chương trình nhập thứ trong tuần'''
while True:
    day=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    choice=int(input("Nhập thứ (1->7):"))
    if 0<choice<8:
        print(choice,":",day[choice-1])
    else:
        print("Thứ không hợp lệ nhập lại")

               


    