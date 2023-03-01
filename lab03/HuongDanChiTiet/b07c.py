h = int(input('Nhập chiều cao tam giác số :'))
# Khởi tạo số bắt đầu
num = 1
# vòng lặp ngoài để xử lý số hàng
for dong in range(1, h+1):
    # gán lại số
    num = 1
    # Vòng lặp tron để xử lý các cột giá trị thay đổi theo
    # vòng lặp ngoài
    for cot in range(1, dong+1):
        # in số
        print(num, end=" ")
        # số tăng dần ở mỗi cột
        num = num + 1
        # dòng kết thúc sau mỗi hàng
    print("\r")
