list_values = []

while True:
    value = input("Nhập giá trị (nhập 'q' để dừng): ")
    if value == 'q':
        break
    list_values.append(value)

print("Danh sách các giá trị:", list_values)
