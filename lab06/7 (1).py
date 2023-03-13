# Tạo List và in các phần tử của List_ ra màn hình.
lst = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], 
["sun", 120]]
print("Các phần tử của list:",lst)
print("Vị trí thứ 3 phần tử thứ 2 của sublist:",(lst[2])[1])
# Kiểm tra độ dài của list test và thêm một sublist ngẫu nhiên
print("Độ dài của list =",len(lst))
lst1=["one",155]
lst.append(lst1)
print("Thêm 1 sublist ngẫu nhiên:\n",lst)
# Thực hiện tính toán tổng sale value trong các ngày thứ 2, thứ 3, thứ 7 và chủ nhật
thu_2=(lst[0])[1]
thu_3=(lst[1])[1]
c_nhat=(lst[6])[1]
tong=thu_2+thu_3+c_nhat
print("Tổng value trong các các ngày thứ 2, thứ 3, chủ nhật =",tong)
