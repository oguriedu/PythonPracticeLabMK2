read = ["một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
number = int(input("Nhập số có 3 chữ số: "))
if 100 <= number <= 999:
    hundred = number // 100
    ten = number % 100 // 10
    unit = number % 10
    if(unit == 0):
        if(ten == 0):
            read_number = read[hundred-1] + " trăm "
        else:
            read_number = read[hundred-1] + " trăm " + read[ten - 1] + " mươi "
    else:
        if(ten == 0):
            read_number = read[hundred-1] + " trăm linh " + read[unit - 1]
        else:
            read_number = read[hundred-1] + " trăm " + \
                read[ten - 1] + " mươi " + read[unit - 1]
    print("Số vừa nhập là:", read_number)
else:
    print("Nhập sai giá trị.")
