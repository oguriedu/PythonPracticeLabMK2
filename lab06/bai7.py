import random

List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]

# In các phần tử của List_ ra màn hình
print(List_)

# Phần tử thứ 2, thuộc vị trí thứ 3 của sublist
element = List_[2][1]
print("Phần tử thứ 2, thuộc vị trí thứ 3 của sublist là:", element)

# Kiểm tra độ dài của list test và thêm một sublist ngẫu nhiên
test = []
print("Độ dài của list test là:", len(test))
test.append([random.choice(["mon", "tue", "wed", "thu", "fri", "sat", "sun"]), random.randint(50, 150)])
print("List test sau khi thêm một sublist ngẫu nhiên là:", test)

# Tính tổng sale value trong các ngày thứ 2, thứ 3, thứ 7 và chủ nhật
sum_value = 0
for item in List_:
    if item[0] in ["tue", "wed", "sat", "sun"]:
        sum_value += item[1]
print("Tổng sale value trong các ngày thứ 2, thứ 3, thứ 7 và chủ nhật là:", sum_value)
