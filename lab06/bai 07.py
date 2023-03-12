List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
lst = []
for i in List_:
    print(f"{i[0]} : {i[1]}")
phan_tu_t2 = 0
sum = 0
for i in range(len(List_)):
    if i==2:
        phan_tu_t2=List_[2][1]
    if i==0 or i==1 or i==6 or i==7:
        sum+=List_[2][1]
print('Phần tử thứ 2, thuộc vị trí thứ 3 của sublist là',phan_tu_t2)
print('Tổng sale value trong các ngày thứ 2, thứ 3, thứ 7 và chủ nhật là',sum)
