thang=(1,2,3,4,5,6,7,8,9,10,11,12)
while True:
    n=int(input("Nhập tháng : "))
    lstthang={1:'January',2: 'February',3: 'March',4: 'April' ,5: 'May',6: 'June',7: 'July',8: 'August',9: 'September',10: 'October' ,11: 'November',12: 'December'}
    if n in thang:
        break
    print("nhập tháng sai !! vui lòng nhập lại.")
print(lstthang[n])