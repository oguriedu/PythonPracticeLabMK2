str = input("Nh ập từ bàn phím một chuỗi ký tự Str: ")

count = 0

for i in str : 
    if i.isdigit() == True: count = count + 1

print("Số lượng các ký tự là số trong chuỗi ký tự Str là: ", count)