List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128],
["sun", 120]]
#in các phần tử trong list_ ra màn hình
for i in List_:
    print(i)
#Chọn ra phần từ thứ 2, thuộc vị trí thứ 3 của sublist
a=List_[1]
b=a[1]
print(b)
# Kiểm tra độ dài của list test
print(len(List_))
#thêm một sublist ngẫu nhiên
import random
sl=[]
for j in (0,1):
    c=random.randrange(0,999)
    sl.append(c)
List_.append(sl)
print(List_)
#Thực hiện tính toán tổng sale value trong các ngày thứ 2, thứ 3, thứ 7 và chủ nhật.
tong=0
for k in List_:
    if k[0]=="mon" or k[0]=="tue" or k[0]=="sat" or k[0]=="sun":
        tong+=k[1]
print(tong)
            
