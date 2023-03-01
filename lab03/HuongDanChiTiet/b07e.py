# giá trị khởi tạo tương ứng với giá trị 'A' ASCII
num = 65
h = int(input('Nhập chiều cao tam giác ký tự: '))
# Vòng lặp ngoài xử lý số hàng
for i in range(0, h):
    # vòng lặp trong xử lý các cột
    # giá trị thay đổi theo vòng lặp ngoài
    for j in range(0, i+1):
        # ép kiểu tường minh từ số sang charater
        ch = chr(num)
        # in giá trị ch
        print(ch, end=" ")
    # Tăng giá trị số
    num = num + 1
    # dòng kết thúc sau mỗi hàng
    print("\r")
