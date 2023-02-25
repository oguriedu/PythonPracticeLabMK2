h=int(input("Nhập giá trị chiều cao tam giác cân: "))
k = 2*h -2
for dong in range(1, h+1):
    for cot in range(1, k+1):
        print(end=" ")
    for cot in range(1, dong+1):
        print("*", end=" ")
    k=k-1
    print("\r")
