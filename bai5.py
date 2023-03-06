while True:
    number = int(input("Nhập số bất kỳ: "))
    if number < 0:
        break
    else:
        print("Bạn đã nhập số dương ", number)

print("Bạn đã nhập số âm, chương trình đã kết thúc.")