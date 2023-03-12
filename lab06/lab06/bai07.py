lst=[]
second=0
sum=0
List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
for i in List_:
    print(f"{i[0]}"),(f"{i[1]}")       
for i in range(len(List_)):
    if i==2 :
        second=List_[2][1]
    elif i == 0 or i == 2 or i == 6 or i == 7 :
        sum+=List_[2][1]

print(f"Phần từ thứ 2, thuộc vị trí thứ 3 của sublist là : {second}")
print(f"Tổng sale value trong các ngày thứ 2, thứ 3, thứ 7 và chủ nhật là: {sum}")

