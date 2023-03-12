List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]

print("List_ = ", List_)

#Chọn ra phần từ thứ 2, thuộc vị trí thứ 3 của sublist
element = List_[1][2] 
print("Phần tử thứ 2, vị trí thứ 3 của sublist = ", element)

#Kiểm tra độ dài của list test và thêm một sublist ngẫu nhiên
test = [] 
print("Độ dài của test = ", len(test)) 
test.append(["mon", 88]) 
print("List test sau khi thêm 1 sublist ngẫu nhiên là = ", test)

#Tính toán tổng sale value trong các ngày thứ 2, thứ 3, thứ 7 và chủ nhật
sum_sale = 0 
for day in List_: 
    if day[0] == "tue" or day[0] == "wed" or day[0] == "sat" or day[0] == "sun": sum_sale += day[1]

print("Tổng sale value trong các ngày thứ 2, thứ 3, thứ 7 và chủ nhật là", sum_sale) 