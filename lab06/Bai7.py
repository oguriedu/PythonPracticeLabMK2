List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
for sublist in List_:
    print(sublist)
element = List_[2][1]
print(element)
# Kiểm tra độ dài của list List_
print(len(List_))

# Thêm một sublist ngẫu nhiên
import random
random_sublist = ["random", random.randint(0, 100)]
List_.append(random_sublist)

# Kiểm tra lại độ dài của list List_ sau khi thêm sublist mới
print(len(List_))
# Tính toán tổng sale value trong các ngày thứ 2, thứ 3, thứ 7 và chủ nhật
sum_sale = 0
for sublist in List_:
    if sublist[0] == "mon":
        continue
    elif sublist[0] == "tue":
        sum_sale += sublist[1]
    elif sublist[0] == "wed":
        sum_sale += sublist[1]
    elif sublist[0] == "thu":
        continue
    elif sublist[0] == "fri":
        continue
    elif sublist[0] == "sat":
        sum_sale += sublist[1]
    elif sublist[0] == "sun":
        sum_sale += sublist[1]

print(sum_sale)
