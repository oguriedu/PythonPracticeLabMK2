List_ = [["mon", 73], ["tue", 89], ["wed", 95], [
    "thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print(List_)
for item in List_:
    print(item)

# Chọn phần tử thứ 2 của sublist thứ 3
print("Phần tử thứ 2 của sublist thứ 3 là:", List_[2][1])

# Kiểm tra độ dài của list và thêm một sublist ngẫu nhiên
print("Độ dài của List_:", len(List_))
List_.append(["new_day", 150])
print("List_ sau khi thêm:", List_)

# Tính tổng sale trong các ngày thứ 2, thứ 3, thứ 7 và chủ nhật
total_sale = 0
for item in List_:
    if item[0] == "mon" or item[0] == "tue" or item[0] == "sat" or item[0] == "sun":
        total_sale = total_sale + item[1]
print("Tổng sale trong các ngày thứ 2, thứ 3, thứ 7 và chủ nhật:", total_sale)
