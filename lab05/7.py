a='''cuộc sống này vốn dĩ là muôn màu muôn vẻ, mỗi người đều có những hoàn cảnh cần đối diện.
 trong mỗi một khoảnh khắc của cuộc sống, họ đều có cho mình những suy nghĩ, hành động riêng.
   Có thể người ngoài nhìn vào sẽ thấy cách mà họ nhìn nhận vấn đề chưa phải là tốt nhất.
     Nhưng với người trong cuộc thì đó là cách giải quyết, hướng đi phù hợp nhất mà họ có thể lựa chọn.
'''
find=input('Nhập từ đơn cần tìm ; ').lower()
lst=a.lower().split()
b=0
for i in lst:
    if i == find:
        b+=1
print('Số từ đơn xuất hiện trong đoạn zvăn trên là : ',b)        