test_1 = [chr(value) for value in range(97, 123)]
test_2 = [str(num) for num in range(0, 10)]
test_3 = [chr(value) for value in range(65, 91)]
test_4 = ["$", "#", "@"]

pwd_list = []
while True:
    pwd = input("Nhap password (enter de dung): ")
    if not pwd:
        break
    else:
        pwd_list.append(pwd)
print(pwd)
valid_pwd = []
for pwd in pwd_list:
    check_test_1 = False
    check_test_2 = False
    check_test_3 = False
    check_test_4 = False
    check_test_5 = len(pwd) > 6 and len(pwd) < 12
    for char in pwd:
        if char in test_1:
            check_test_1 = True
        if char in test_2:
            check_test_2 = True
        if char in test_3:
            check_test_3 = True
        if char in test_4:
            check_test_4 = True
    if check_test_1 == True and check_test_2 == True and check_test_3 == True and check_test_4 == True and check_test_5 == True:
        valid_pwd.append(pwd)
print("Danh sach hop le: ")
print(valid_pwd)
