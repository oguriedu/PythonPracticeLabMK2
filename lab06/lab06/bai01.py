lst=[2,-4,1,9,-3,6,3,-2,6,8]
num=0
tong_gia_tri=sum(lst)
print(tong_gia_tri)
so_nguyen_duong=[num for num in lst if num >=0]
print("so nguyen duong trong list la :",so_nguyen_duong)
print("phần tử âm đầu tiên trong list là :",lst[1])
print("phần tử dương cuối cùng trong danh sách là :",lst[9])
print("phần tử lớn nhất trong líst là :",max(lst)," và vị trí của phần tử làm ở thứ",lst[3])