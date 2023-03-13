n = int(input("Nhập giá trị n ="))
li = []
for i in range(1, n+1):
    li.append(i)


def check_so_nguyen_to(x):
    flag = True
    if x < 2:
        flag = False
    else:
        for i in range(2, x):
            if x % i == 0:
                flag = False
                break
    return flag


print("Danh sách các số nguyên tố thuộc li là: ")
for j in li:
    if check_so_nguyen_to(j):
        print(j, end=' ')
        pos = str.rfind(" ")
print("Tên sinh viên là:", str[pos+1:])
