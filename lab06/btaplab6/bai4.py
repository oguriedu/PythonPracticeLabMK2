lst = []
while True:
    num = int(input("Nhập một số tự nhiên (nhập 0 để kết thúc): "))
    if num == 0:
        break
    lst.append(num)
print("Danh sách đã nhập:", lst)
num=[1,2,3]
#chèn vào cuối
lst.append(num)
#chèn vào đầu
lst.insert(0,num)
#chèn vào vị trí thứ 5
lst.insert(5,num)
print("list sau khi chèn thêm là ",lst)