# Nhập chuỗi S1 và S2 từ người dùng
S1 = input("Nhập chuỗi S1: ")
S2 = input("Nhập chuỗi S2: ")

# Tính số lần xuất hiện của S2 trong S1 (có chồng lấn)
count_overlap = 0  # biến đếm số lần xuất hiện S2 trong S1(có chồng lấn)
start = 0
while True:
    # trả về vị trí xuất hiện của S2 trong S1 từ vị trí start
    start = S1.find(S2, start)
    if start == -1:
        break
    count_overlap += 1
    start += 1

# Tính số lần xuất hiện của S2 trong S1 (không chồng lấn)
count_non_overlap = 0  # biến đếm số lần xuất hiện S2 trong S1(có chồng lấn)
start = 0
while True:
    start = S1.find(S2, start)
    if start == -1:
        break
    count_non_overlap += 1
    start = start + len(S2)

# In kết quả
if count_overlap == 0:
    print("Chuỗi S2 không nằm trong chuỗi S1")
else:
    print("Chuỗi S2 có nằm trong chuỗi S1")
    print("S2 xuất hiện trong S1 (có chồng lấn) ", count_overlap, "lần")
    print("S2 xuất hiện trong S1 (không chồng lấn) ", count_non_overlap, "lần")
