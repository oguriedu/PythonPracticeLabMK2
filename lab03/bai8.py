h = int(input("Nhập giá trị chiều cao tam giác cân: "))
#Xác định khoảng trắng 
k =2*h-2
# Vòng lặp bên ngoài xác định số dòng
for dong in range(1,h+1):
    # Vòng lặp trong để xác định số khoảng trắng
    # Thay đổi các giá trị tuỳ yêu cầu 
    for cot in range(1,k+1):
        #In số dấu cách
        print(end=" ")
        #Vòng lặp bên trong để xử lý số lượng giá trị cột
        # thay đổi theo vòng lặp bên ngoài 
    for cot in range(1,dong+1):
        # in 
        print("*",end=" ")
        #giảm k đi 1 sau mỗi lần kết thúc dòng
    k =k-1
    print("\r")