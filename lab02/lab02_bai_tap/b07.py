score = float(input("Nhập vào điểm TK: "))

if score >= 0 and score < 4:
    print("Loại Kém")
elif score == 4:
    print("Loại Yếu")
elif score >= 5 and score < 7:
    print("Loại Trung Bình")
elif score >= 7 and score < 9:
    print("Loại Khá")
elif score >= 9 and score <= 10:
    print("Loại Giỏi")
else:
    print("Điểm TK không hợp lệ")