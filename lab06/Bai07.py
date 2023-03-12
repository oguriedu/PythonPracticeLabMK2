List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
for i in List_:
    print(f"{i[0]},{i[1]}")
s=0
for i in List_:    
    if i==List_[3]:
        print('Phần tử thứ 2,thuộc vị trí thứ 3: ',i[1])
print('Độ dài list: ',len(List_))
for i in List_:
    if i==List_[0]:
        s+=i[1]
    elif i==List_[1]:
        s+=i[1]  
    elif i==List_[5]:
        s+=i[1]
    elif i==List_[6]:
        s+=i[1]    
print('Tổng sale value trong các ngày thứ 2, 3, 7, cn: ',s)