str = input("Cho trư ớc hoặc nhập từ bàn phím chuỗi ký tự Str: ")

count = 1 
max_count = 0 
max_char = ""

for i in range(len(str)): 
    if i < len(str)-1 and str[i] == str[i+1]: count += 1 
    else: 
        if count > max_count: max_count = count 
        max_char = str[i] 
        count = 1

for i in range(max_count): print(max_char, end="")