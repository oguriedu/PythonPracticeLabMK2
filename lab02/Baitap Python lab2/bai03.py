#chương trình cho biết ngày trong tuần
ngay_trong_tuan = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
while True:
    day = int(input("hãy nhập ngày trong tuần : "))
    if day in ngay_trong_tuan:
        break
    print("bạn đã nhập  sai,hãy nhập lại")

print("Thứ mà bạn đã nhập là:", ngay_trong_tuan[day])