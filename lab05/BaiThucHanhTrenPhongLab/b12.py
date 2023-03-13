while True:
    str_1 = input("Nhập chuỗi số 1: ")
    if str_1.isnumeric():
        break

while True:
    str_2 = input("Nhập chuỗi số 2: ")
    if str_2.isnumeric():
        break
len_str1 = len(str_1)
len_str2 = len(str_2)

if len_str1 == 0 or len_str1 == 1 or len_str2 == 0 or len_str2 == 1:
    print("Không tồn tại cách đặt")
else:
    str_C = ""
    str_D = ""
    str_E = ""
    str_F = ""
    check = False
    for i in range(1, len_str1):
        str_C = str_1[:i]
        str_D = str_1[i:]
        for j in range(1, len_str2):
            str_E = str_2[:j]
            str_F = str_2[j:]
            if int(str_C) + int(str_D) == int(str_E) + int(str_F):
                print(f"{str_C} + {str_D} = {str_E}  + {str_F}")
                check = True
    if check == False:
        print("Không tồn tại cách đặt")
