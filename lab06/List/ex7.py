import random
list = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("List_",list)
sublist = list[2]
local = sublist [1]
print("Phần tử thứ 2, thuộc vị trí thứ 3 của sublist:", local)
print("Độ dài của List:", len(list))
new_sublist = ["new_day", random.randint(50, 200)]
list.append(new_sublist)
print(list)
#tinh value
value=0
day = ["mon","tue","sat","sun"]
for i in list:
    for i[0] in day:
        value += i[1]
print("Tổng sale value của các ngày thứ 2, thứ 3, thứ 7 và chủ nhật là:", value)