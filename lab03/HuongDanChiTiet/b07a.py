h = int(input("Nhập chiều cao tam giác: "))
# Vòng lặp bên ngoài xác định số dòng, trong bài này là h
for i in range(0, h):
    # Vòng lặp bên trong giữ số cột có
    # các giá trị thay đổi đối với vòng lặp ngoài
    for j in range(0, i+1):
        # in các trạng thái
        print("* ", end='')

    # Kết thúc sau mỗi dòng
    print("\r")  # '\r' xuống dòng và đưa con trỏ về đầu dòng
