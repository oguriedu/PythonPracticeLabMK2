 # Hàm lambda để xác định cách sắp xếp cho mỗi tuple
sort_key = lambda tup: (tup[0], tup[1], tup[2])

# Nhập vào list các tuples
lst = []
while True:
    inp = input("Nhập vào một tuple (name, age, score): ")
    if inp == "":
        break
    else:
        try:
            name, age, score = inp.split(",")
            lst.append((name.strip(), int(age.strip()), int(score.strip())))
        except:
            print("Lỗi: Vui lòng nhập đúng định dạng (name, age, score)")

# Sắp xếp list các tuples
sorted_lst = sorted(lst, key=sort_key)

# In ra các tuples đã sắp xếp
for tup in sorted_lst:
    print(tup)
