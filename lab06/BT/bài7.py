List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], 
["sun", 120]]
for i in List_:
    print(f"{i[0]} : {i[1]}")
pt2=0
sum=0
for i in range(len(List_)):
    if i==2:
        pt2=List_[2][1]
    if i==0 or i==1 or i==6 or i==7:
        sum+=List_[2][1]
print(pt2)
print(sum)
